#!/usr/bin/env python3
"""Check the packaged short-drama skills against the source snapshot."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
LOCK = ROOT / 'skills.lock.json'

def tree_digest(directory: Path) -> str:
    digest = hashlib.sha256()
    for path in sorted(p for p in directory.rglob('*') if p.is_file()):
        digest.update(path.relative_to(directory).as_posix().encode() + b'\0')
        digest.update(path.read_bytes())
    return digest.hexdigest()

def main() -> int:
    lock = json.loads(LOCK.read_text())
    expected = lock['skills']
    actual = {p.name for p in (ROOT / 'skills').iterdir() if p.is_dir()}
    if actual != set(expected):
        print(f'skill set mismatch: expected={sorted(expected)} actual={sorted(actual)}')
        return 1
    for name, sha in expected.items():
        if tree_digest(ROOT / 'skills' / name) != sha:
            print(f'{name}: hash mismatch')
            return 1
    print(f'OK: {len(expected)} skills match dreamina-skills {lock["sourceCommit"][:12]}')
    return 0

if __name__ == '__main__':
    sys.exit(main())
