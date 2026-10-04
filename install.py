"""Install the complete skill bundle into a host skill root; refuse conflicts."""
import argparse
import os
from pathlib import Path
import shutil
import sys

def files(root):
    return {str(p.relative_to(root)):p.read_bytes() for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc'}

def install(destination, dry_run=False):
    source=Path(__file__).resolve().parent/'skills'
    skills=sorted(p for p in source.iterdir() if (p/'SKILL.md').is_file())
    conflicts=[p.name for p in skills if (destination/p.name).exists() and files(p)!=files(destination/p.name)]
    if conflicts: raise ValueError('Existing skills differ; no files changed: '+', '.join(conflicts))
    pending=[p for p in skills if not (destination/p.name).exists()]
    if not dry_run:
        destination.mkdir(parents=True,exist_ok=True)
        for p in pending: shutil.copytree(p,destination/p.name,ignore=shutil.ignore_patterns('__pycache__','*.pyc'))
    return {'skill_count':len(skills),'new_skills':len(pending),'destination':str(destination),'dry_run':dry_run}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--target',choices=['claude','codex'])
    parser.add_argument('--dest',type=Path)
    parser.add_argument('--dry-run',action='store_true')
    args=parser.parse_args()
    if args.dest is None and args.target is None: parser.error('choose --target or --dest')
    if args.dest is not None: destination=args.dest.expanduser().resolve()
    elif args.target=='claude': destination=Path.home()/'.claude/skills'
    else: destination=Path(os.environ.get('CODEX_HOME',str(Path.home()/'.codex')))/'skills'
    import json
    print(json.dumps(install(destination,args.dry_run),indent=2))

if __name__=='__main__':
    try: main()
    except (ValueError,OSError) as error:
        print(str(error),file=sys.stderr); sys.exit(2)
