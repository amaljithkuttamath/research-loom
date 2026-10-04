import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('loom_installer',ROOT/'install.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.dest=Path(self.temp.name)/'skills'
    def test_dry_run_does_not_write(self):
        result=module.install(self.dest,True)
        self.assertEqual(result['skill_count'],10);self.assertFalse(self.dest.exists())
    def test_install_and_reinstall_are_idempotent(self):
        module.install(self.dest)
        self.assertEqual(len(list(self.dest.glob('*/SKILL.md'))),10)
        self.assertTrue((self.dest/'research-loom/scripts/project_config.py').exists())
        self.assertEqual(module.install(self.dest)['new_skills'],0)
    def test_conflicts_stop_before_other_writes(self):
        folder=self.dest/'research-loom';folder.mkdir(parents=True)
        path=folder/'SKILL.md';path.write_text('existing custom skill')
        with self.assertRaises(ValueError):module.install(self.dest)
        self.assertEqual(path.read_text(),'existing custom skill')
        self.assertEqual(len(list(self.dest.iterdir())),1)

if __name__=='__main__':unittest.main()
