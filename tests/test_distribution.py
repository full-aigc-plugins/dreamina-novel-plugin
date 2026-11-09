import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    'dreamina-novel-cli', 'dreamina-novel-cli-setup', 'dreamina-novel-cli-script',
    'dreamina-novel-cli-assets', 'dreamina-novel-cli-storyboard',
    'dreamina-novel-cli-production', 'dreamina-novel-cli-post', 'dreamina-novel-use',
}


class DistributionTests(unittest.TestCase):
    def test_all_eight_skills_are_packaged(self):
        self.assertEqual({path.name for path in (ROOT / 'skills').iterdir() if path.is_dir()}, EXPECTED)
        for name in EXPECTED:
            text = (ROOT / 'skills' / name / 'SKILL.md').read_text(encoding='utf-8')
            self.assertIn(f'name: {name}', text)
            self.assertTrue((ROOT / 'skills' / name / 'agents' / 'openai.yaml').is_file())

    def test_manifests_agree_on_identity_and_version(self):
        portable = json.loads((ROOT / 'plugin.json').read_text())
        codex = json.loads((ROOT / '.codex-plugin/plugin.json').read_text())
        zcode = json.loads((ROOT / '.zcode-plugin/plugin.json').read_text())
        kimi = json.loads((ROOT / 'kimi.plugin.json').read_text())
        self.assertEqual(portable['name'], 'dreamina-novel')
        for manifest in (codex, zcode, kimi):
            self.assertEqual(manifest['name'], portable['name'])
            self.assertEqual(manifest['version'].split('+', 1)[0], portable['version'])
        self.assertEqual(codex['skills'], './skills/')

    def test_vendored_skills_match_lock(self):
        result = subprocess.run([sys.executable, str(ROOT / 'scripts/verify_vendored_skills.py')], capture_output=True, text=True)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)

    def test_paid_and_recovery_rules_are_present(self):
        production = (ROOT / 'skills/dreamina-novel-cli-production/SKILL.md').read_text()
        self.assertIn('credit estimate', production)
        self.assertIn('node result', production)
        self.assertIn('用户确认', production)
        script = (ROOT / 'skills/dreamina-novel-cli-script/SKILL.md').read_text()
        self.assertIn('thread_id', script)
        self.assertIn('run_id', script)


if __name__ == '__main__':
    unittest.main()
