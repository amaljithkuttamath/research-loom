"""Resolve project-specific skill selections. No model or external-service dependency."""
import argparse
import copy
import json
import os
from pathlib import Path
import re
import sys
import tempfile
import uuid

DEFAULT_FILE = Path(__file__).resolve().parents[1] / 'assets/project-config.json'
STAGES = ('interview', 'narrow', 'search-plan', 'synthesize', 'outline', 'draft', 'review')
SKILL_NAME = re.compile(r'^[a-z0-9][a-z0-9-]{0,63}$')

def atomic_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix='.pending-', dir=path.parent)
    try:
        with os.fdopen(fd, 'w') as stream:
            json.dump(data, stream, indent=2)
            stream.write('\n')
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temporary, path)
    finally:
        if os.path.exists(temporary): os.unlink(temporary)

def load(path):
    with path.open() as stream: return json.load(stream)

def selections(value):
    if not isinstance(value, dict): raise ValueError('stages must be an object')
    for key, name in value.items():
        if key not in STAGES: raise ValueError(f'unknown stage: {key}')
        if not isinstance(name, str) or not SKILL_NAME.fullmatch(name):
            raise ValueError(f'invalid skill name for stage {key}')

def branches(value):
    if not isinstance(value, list) or not value: raise ValueError('search_branches must be a nonempty array')
    seen = set()
    for branch in value:
        if not isinstance(branch, dict): raise ValueError('each branch must be an object')
        for key in ('id', 'skill', 'source'):
            if not isinstance(branch.get(key), str) or not branch[key].strip():
                raise ValueError(f'branch {key} must be a nonempty string')
        if branch['id'] in seen: raise ValueError(f'duplicate branch ID: {branch["id"]}')
        seen.add(branch['id'])
        if not SKILL_NAME.fullmatch(branch['skill']): raise ValueError('invalid branch skill name')

def validate(config, project):
    if not isinstance(config, dict) or config.get('version') != 1: raise ValueError('unsupported configuration version')
    if config.get('project_root') != str(project):
        raise ValueError('configuration belongs to another project location; explicit relocation is required')
    if not isinstance(config.get('project_id'), str) or not config['project_id']:
        raise ValueError('missing project_id')
    selections(config.get('stages', {}))
    branches(config['search_branches'])
    goals = config.get('goals', [])
    if not isinstance(goals, list): raise ValueError('goals must be an array')
    seen = set()
    for goal in goals:
        if not isinstance(goal, dict) or not isinstance(goal.get('id'), str) or not goal['id']:
            raise ValueError('each goal requires a nonempty ID')
        if goal['id'] in seen: raise ValueError('duplicate goal ID')
        seen.add(goal['id'])
        selections(goal.get('stages', {}))
        if 'search_branches' in goal: branches(goal['search_branches'])

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action', choices=['init', 'resolve'])
    parser.add_argument('--project')
    parser.add_argument('--goal')
    args = parser.parse_args()
    project = Path(args.project or os.environ.get('RLOOM_PROJECT') or Path.cwd()).expanduser().resolve()
    folder = project / '.research-loom'
    config_path = folder / 'config.json'
    defaults = load(DEFAULT_FILE)
    if args.action == 'init':
        if not config_path.exists():
            config = copy.deepcopy(defaults)
            config['project_id'] = str(uuid.uuid4())
            config['project_root'] = str(project)
            atomic_json(config_path, config)
        config = load(config_path)
        validate(config, project)
        state_path = folder / 'state.json'
        if not state_path.exists():
            atomic_json(state_path, {'version':1, 'project_id':config['project_id'], 'brief':{}, 'confirmed_questions':{}, 'nodes':{}, 'active_node':None, 'next_action':'interview'})
        elif load(state_path).get('project_id') != config['project_id']:
            raise ValueError('state belongs to a different project')
        print(json.dumps({'config_path':str(config_path), 'state_path':str(state_path), 'project_id':config['project_id']}))
        return
    config = load(config_path)
    validate(config, project)
    stages = defaults['stages'] | config.get('stages', {})
    selected_branches = copy.deepcopy(config['search_branches'])
    origins = {key:'project' if key in config.get('stages', {}) else 'default' for key in stages}
    if args.goal:
        goal = next((g for g in config.get('goals',[]) if g['id']==args.goal),None)
        if goal is None: raise ValueError(f'unknown goal: {args.goal}')
        stages.update(goal.get('stages',{}))
        origins.update({key:'goal' for key in goal.get('stages',{})})
        if 'search_branches' in goal: selected_branches=copy.deepcopy(goal['search_branches'])
    overrides = {}
    for stage in STAGES:
        name = 'RLOOM_STAGE_' + stage.upper().replace('-','_')
        if name in os.environ:
            stages[stage]=os.environ[name]; origins[stage]='environment'; overrides[name]=os.environ[name]
    if 'RLOOM_SEARCH_BRANCHES' in os.environ:
        selected_branches=json.loads(os.environ['RLOOM_SEARCH_BRANCHES'])
        overrides['RLOOM_SEARCH_BRANCHES']=selected_branches
    selections(stages); branches(selected_branches)
    print(json.dumps({'project_id':config['project_id'], 'project_root':str(project), 'goal_id':args.goal, 'stages':stages, 'search_branches':selected_branches, 'selection_origins':origins, 'environment_overrides':overrides},indent=2))

if __name__=='__main__':
    try: main()
    except (ValueError, KeyError, OSError, TypeError) as error:
        print(f'Configuration error: {error}',file=sys.stderr)
        sys.exit(2)
