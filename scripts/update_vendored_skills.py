#!/usr/bin/env python3
"""Copy the eight managed short-drama skills from a clean source checkout."""
import argparse
import json
import shutil
import subprocess
from pathlib import Path
from verify_vendored_skills import tree_digest

ROOT = Path(__file__).resolve().parents[1]
SKILLS = (
    'dreamina-novel-cli', 'dreamina-novel-cli-setup', 'dreamina-novel-cli-script',
    'dreamina-novel-cli-assets', 'dreamina-novel-cli-storyboard',
    'dreamina-novel-cli-production', 'dreamina-novel-cli-post', 'dreamina-novel-use',
)


def git(source: Path, *args: str) -> str:
    return subprocess.check_output(['git', '-C', str(source), *args], text=True).strip()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--expected-commit', required=True)
    args = parser.parse_args()
    source = args.source.resolve()
    commit = git(source, 'rev-parse', 'HEAD')
    if commit != args.expected_commit:
        raise SystemExit(f'expected {args.expected_commit}, source is {commit}')
    if git(source, 'status', '--porcelain'):
        raise SystemExit('source checkout has uncommitted changes')
    version = json.loads((source / '.claude-plugin/plugin.json').read_text())['version']
    if version != '1.8.0':
        raise SystemExit(f'unexpected source version: {version}')
    if subprocess.run(['git', '-C', str(ROOT), 'rev-parse', '--verify', 'HEAD'], capture_output=True).returncode == 0:
        if git(ROOT, 'status', '--porcelain', '--', 'skills'):
            raise SystemExit('managed plugin skills have uncommitted changes')
    for name in SKILLS:
        origin = source / 'skills' / name
        if not (origin / 'SKILL.md').is_file():
            raise SystemExit(f'missing source skill: {name}')
        target = ROOT / 'skills' / name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(origin, target)
    lock_path = ROOT / 'skills.lock.json'
    old_commit = json.loads(lock_path.read_text()).get('sourceCommit') if lock_path.exists() else None
    lock = {
        'version': 1,
        'sourcePackage': 'dreamina-skills',
        'sourceRepository': 'https://github.com/full-aigc-skills/dreamina-skills.git',
        'sourceCommit': commit,
        'sourceVersion': version,
        'releaseStatus': 'unpublished-local-snapshot',
        'skills': {name: tree_digest(ROOT / 'skills' / name) for name in SKILLS},
    }
    lock_path.write_text(json.dumps(lock, ensure_ascii=False, indent=2) + '\n')
    for filename in ('README.md', 'README.zh-CN.md'):
        readme = ROOT / filename
        text = readme.read_text()
        if old_commit:
            text = text.replace(old_commit, commit)
        readme.write_text(text)
    print(f'updated {len(SKILLS)} skills from {commit}')


if __name__ == '__main__':
    main()
