import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / 'scripts/project_config.py'

class ProjectConfigTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.a = Path(self.temp.name) / 'a'
        self.b = Path(self.temp.name) / 'b'
        self.env = {k:v for k,v in os.environ.items() if not k.startswith('RLOOM_')}
    def run_cli(self, action, project=None, goal=None, env=None, ok=True):
        args = ['python3', str(SCRIPT), action]
        if project is not None: args += ['--project', str(project)]
        if goal: args += ['--goal', goal]
        p = subprocess.run(args, env=self.env | (env or {}), text=True, capture_output=True)
        if ok:
            self.assertEqual(p.returncode, 0, p.stderr)
            return json.loads(p.stdout)
        self.assertNotEqual(p.returncode, 0)
        return p
    def init(self, p): self.run_cli('init', p)
    def edit(self, p, fn):
        path = p / '.research-loom/config.json'
        d = json.loads(path.read_text()); fn(d); path.write_text(json.dumps(d))
    def test_init_and_resolve_defaults(self):
        self.init(self.a)
        self.assertEqual(self.run_cli('resolve', self.a)['stages']['interview'], 'research-loom-interview')
    def test_saved_choice_survives_new_process(self):
        self.init(self.a)
        self.edit(self.a, lambda d:d['stages'].update(draft='custom-draft'))
        self.assertEqual(self.run_cli('resolve', self.a)['stages']['draft'], 'custom-draft')
    def test_environment_override_is_temporary(self):
        self.init(self.a)
        path = self.a / '.research-loom/config.json'; before=path.read_bytes()
        self.assertEqual(self.run_cli('resolve', self.a, env={'RLOOM_STAGE_DRAFT':'temporary-draft'})['stages']['draft'],'temporary-draft')
        self.assertEqual(path.read_bytes(),before)
        self.assertEqual(self.run_cli('resolve', self.a)['stages']['draft'],'research-loom-draft')
    def test_projects_are_isolated(self):
        self.init(self.a); self.init(self.b)
        self.edit(self.a,lambda d:d['stages'].update(draft='only-a'))
        self.assertEqual(self.run_cli('resolve',self.b)['stages']['draft'],'research-loom-draft')
    def test_goal_overrides_then_environment(self):
        self.init(self.a)
        self.edit(self.a,lambda d:d.update(goals=[{'id':'g1','question':'Q','stages':{'draft':'goal-draft'}}]))
        self.assertEqual(self.run_cli('resolve',self.a,'g1')['stages']['draft'],'goal-draft')
        self.assertEqual(self.run_cli('resolve',self.a,'g1',{'RLOOM_STAGE_DRAFT':'env-draft'})['stages']['draft'],'env-draft')
    def test_many_search_branches(self):
        self.init(self.a)
        branches=[{'id':f'b{i}','skill':'research-loom-search','source':f'source{i}'} for i in range(12)]
        self.assertEqual(self.run_cli('resolve',self.a,env={'RLOOM_SEARCH_BRANCHES':json.dumps(branches)})['search_branches'],branches)
    def test_malformed_override_rejected(self):
        self.init(self.a)
        self.run_cli('resolve',self.a,env={'RLOOM_SEARCH_BRANCHES':'broken'},ok=False)
    def test_duplicate_branch_id_rejected(self):
        self.init(self.a)
        b={'id':'same','skill':'research-loom-search','source':'auto'}
        self.run_cli('resolve',self.a,env={'RLOOM_SEARCH_BRANCHES':json.dumps([b,b])},ok=False)
    def test_unknown_goal_rejected(self):
        self.init(self.a); self.run_cli('resolve',self.a,'absent',ok=False)
    def test_init_preserves_existing_state(self):
        self.init(self.a)
        path=self.a/'.research-loom/state.json'
        d=json.loads(path.read_text()); d['next_action']='resume interview'; path.write_text(json.dumps(d))
        before=path.read_bytes(); self.init(self.a); self.assertEqual(path.read_bytes(),before)
    def test_copied_config_identity_rejected(self):
        self.init(self.a); self.init(self.b)
        path=self.b/'.research-loom/config.json'
        path.write_bytes((self.a/'.research-loom/config.json').read_bytes())
        self.run_cli('resolve',self.b,ok=False)
    def test_explicit_project_beats_environment(self):
        self.init(self.a); self.init(self.b)
        self.assertEqual(self.run_cli('resolve',self.a,env={'RLOOM_PROJECT':str(self.b)})['project_root'],str(self.a.resolve()))

if __name__=='__main__': unittest.main()
