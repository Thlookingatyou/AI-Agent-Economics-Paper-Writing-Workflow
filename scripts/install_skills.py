"""Optional project-local Claude copies, with no global configuration edits."""
import argparse
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]


def install(update=False):
    messages = []
    base = (ROOT / '.claude/skills').resolve()
    if not base.is_relative_to(ROOT.resolve()):
        raise ValueError('Project skill copies must stay inside this repository.')
    for source in sorted((ROOT / '.agents/skills').iterdir()):
        if not source.is_dir():
            continue
        target = ROOT / '.claude/skills' / source.name
        if target.exists():
            if not update:
                messages.append(f'Skipped existing {source.name}; use --update to replace local copies.')
                continue
            if target.is_symlink() or not target.resolve().is_relative_to(ROOT / '.claude/skills'):
                raise ValueError('Refusing to replace a symlinked/external skill.')
            shutil.rmtree(target)
        shutil.copytree(source, target)
        messages.append('Copied ' + source.name)
    return messages


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--target', choices=['claude'], required=True)
    ap.add_argument('--update', action='store_true')
    args = ap.parse_args()
    print('\n'.join(install(args.update)))
