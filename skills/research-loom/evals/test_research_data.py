import copy
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from research_data import validate

# Deliberately fictional fixture; never publish as real research.
FIXTURE={'schema_version':1,'papers':[{'id':'p1','title':'Fictional fixture','authors':['Fixture author'],'identifiers':{},'versions':[{'id':'v1','url':'https://example.org/fixture','publication_status':'preprint','read_level':'abstract','checked_at':'2026-10-04T12:00:00Z'}]}], 'searches':[{'id':'s1','goal_id':'g1','branch_id':'b1','source':'fixture','query':'fixture query','status':'executed','executed_at':'2026-10-04T12:00:00Z','hits':[{'paper_id':'p1','version_id':'v1'}]}], 'claims':[{'id':'c1','goal_id':'g1','text':'Fictional abstract-level claim','status':'supported','evidence':[{'paper_id':'p1','version_id':'v1','locator':'Abstract','read_level':'abstract','relation':'supports','verification':'verified','verified_at':'2026-10-04T12:00:00Z'}]}]}

class ResearchDataTests(unittest.TestCase):
    def setUp(self): self.data=copy.deepcopy(FIXTURE)
    def reject(self):
        with self.assertRaises(ValueError): validate(self.data)
    def test_valid_linked_records(self):
        self.assertEqual(validate(self.data),{'papers':1,'searches':1,'claims':1})
    def test_dangling_paper_link(self):
        self.data['searches'][0]['hits'][0]['paper_id']='missing'; self.reject()
    def test_dangling_version_link(self):
        self.data['claims'][0]['evidence'][0]['version_id']='missing'; self.reject()
    def test_abstract_cannot_support_full_text_extraction(self):
        self.data['claims'][0]['evidence'][0]['read_level']='full_text'; self.reject()
    def test_supported_claim_requires_verified_support(self):
        self.data['claims'][0]['evidence'][0]['verification']='unverified'; self.reject()
    def test_duplicate_ids_rejected(self):
        self.data['papers'].append(copy.deepcopy(self.data['papers'][0])); self.reject()
    def test_planned_search_is_not_executed(self):
        self.data['searches'][0]['status']='planned'; self.reject()
    def test_execution_requires_timestamp(self):
        del self.data['searches'][0]['executed_at']; self.reject()
    def test_versions_and_repeat_discovery_preserved(self):
        version=copy.deepcopy(self.data['papers'][0]['versions'][0]); version['id']='v2'; version['publication_status']='published'
        self.data['papers'][0]['versions'].append(version)
        search=copy.deepcopy(self.data['searches'][0]); search['id']='s2'; search['hits'][0]['version_id']='v2'; self.data['searches'].append(search)
        self.assertEqual(validate(self.data)['papers'],1)
        self.assertEqual(validate(self.data)['searches'],2)
    def test_contradictions_can_be_retained(self):
        link=copy.deepcopy(self.data['claims'][0]['evidence'][0]); link['relation']='contradicts'
        self.data['claims'][0]['status']='disputed'; self.data['claims'][0]['evidence'].append(link)
        self.assertEqual(validate(self.data)['claims'],1)
    def test_verification_requires_timestamp(self):
        del self.data['claims'][0]['evidence'][0]['verified_at']; self.reject()

if __name__=='__main__': unittest.main()
