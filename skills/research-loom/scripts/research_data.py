"""Validate simple paper/search/claim JSON and their references."""
import argparse
import json
from pathlib import Path
import sys
from project_config import atomic_json

LEVELS = {'metadata':0, 'abstract':1, 'full_text':2}

def require(record, fields, context):
    if not isinstance(record,dict): raise ValueError(f'{context} must be an object')
    for field in fields:
        if not isinstance(record.get(field),str) or not record[field].strip():
            raise ValueError(f'{context}.{field} must be a nonempty string')

def enum(record, field, choices, context):
    if record.get(field) not in choices: raise ValueError(f'{context}.{field} must be one of {sorted(choices)}')

def unique(records, context):
    if not isinstance(records,list): raise ValueError(f'{context} must be an array')
    indexed={}
    for record in records:
        require(record,['id'],context)
        if record['id'] in indexed: raise ValueError(f'duplicate {context} ID: {record["id"]}')
        indexed[record['id']]=record
    return indexed

def validate(data):
    if not isinstance(data,dict) or data.get('schema_version') != 1: raise ValueError('unsupported schema_version')
    papers=unique(data.get('papers'),'papers')
    searches=unique(data.get('searches'),'searches')
    claims=unique(data.get('claims'),'claims')
    versions={}
    for paper in papers.values():
        require(paper,['title'],'paper')
        if not isinstance(paper.get('authors'),list) or not all(isinstance(x,str) and x for x in paper['authors']):
            raise ValueError('paper.authors must be an array of names')
        if not isinstance(paper.get('identifiers'),dict): raise ValueError('paper.identifiers must be an object')
        pv=unique(paper.get('versions'),'versions')
        if not pv: raise ValueError('paper must have at least one version')
        for version in pv.values():
            require(version,['url','checked_at'],'version')
            enum(version,'publication_status',{'preprint','published','corrected','retracted','unknown'},'version')
            enum(version,'read_level',LEVELS,'version')
            versions[(paper['id'],version['id'])]=version
    def target(link):
        require(link,['paper_id','version_id'],'link')
        key=(link['paper_id'],link['version_id'])
        if key not in versions: raise ValueError(f'unknown paper/version link: {key}')
        return versions[key]
    for search in searches.values():
        require(search,['goal_id','branch_id','source','query'],'search')
        enum(search,'status',{'planned','executed','blocked'},'search')
        if search['status']=='executed': require(search,['executed_at'],'search')
        if not isinstance(search.get('hits'),list): raise ValueError('search.hits must be an array')
        if search['status']!='executed' and search['hits']: raise ValueError('unexecuted search cannot have retrieved hits')
        for hit in search['hits']: target(hit)
    for claim in claims.values():
        require(claim,['goal_id','text'],'claim')
        enum(claim,'status',{'unverified','supported','disputed','unsupported'},'claim')
        if not isinstance(claim.get('evidence'),list): raise ValueError('claim.evidence must be an array')
        supported=False
        for link in claim['evidence']:
            version=target(link)
            require(link,['locator'],'evidence')
            enum(link,'read_level',LEVELS,'evidence')
            enum(link,'relation',{'supports','contradicts','context'},'evidence')
            enum(link,'verification',{'verified','unverified'},'evidence')
            if LEVELS[link['read_level']] > LEVELS[version['read_level']]:
                raise ValueError('evidence exceeds actual source reading level')
            if link['verification']=='verified': require(link,['verified_at'],'evidence')
            supported |= link['relation']=='supports' and link['verification']=='verified'
        if claim['status']=='supported' and not supported:
            raise ValueError('supported claim requires verified supporting evidence')
    return {'papers':len(papers),'searches':len(searches),'claims':len(claims)}

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('action',choices=['init','validate'])
    parser.add_argument('--project',type=Path,required=True)
    args=parser.parse_args()
    path=args.project.resolve()/'.research-loom/research.json'
    if args.action=='init' and not path.exists():
        asset=Path(__file__).resolve().parents[1]/'assets/research.json'
        atomic_json(path,json.loads(asset.read_text()))
    result=validate(json.loads(path.read_text()))
    print(json.dumps({'path':str(path),'valid':True,**result}))

if __name__=='__main__':
    try: main()
    except (ValueError,OSError,KeyError,TypeError) as error:
        print(f'Research data error: {error}',file=sys.stderr); sys.exit(2)
