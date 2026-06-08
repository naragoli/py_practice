"""
Reorganize top-level example scripts into the new folder structure.
Run from repository root:
    python scripts/reorganize.py
This script moves files and directories; it will create target folders as needed.
"""
import re
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parent.parent
print('Repository root:', ROOT)

mappings = []

# Move numbered lesson files by prefix
prefix_map = {
    '1': 'examples/01_identifiers',
    '2': 'examples/02_datatypes',
    '3': 'examples/03_strings',
    '4': 'examples/04_operators',
    '5': 'examples/05_io',
    '6': 'examples/06_control_flow',
    '7': 'examples/07_loops',
    '8': 'examples/08_patterns',
    '9': 'examples/09_string_ops',
    '0': 'examples/00_misc'
}

# Prepare directory moves for known folders
folder_moves = {
    'p_time': 'examples/p_time',
    'raw': 'examples/raw',
    'repl': 'examples/repl',
    'reusable_functions': 'src/utils',
    'todo-expo': 'apps/todo-expo'
}

# Build mappings for top-level files
for path in ROOT.iterdir():
    if path.is_dir():
        name = path.name
        if name in folder_moves:
            src = path
            dst = ROOT / folder_moves[name]
            mappings.append((src, dst))
        continue

    # Skip this script and repo files
    if path.name in ('scripts', 'README.md', '.gitignore', 'requirements.txt'):
        continue

    m = re.match(r"^(\d+)\.", path.name)
    if m:
        prefix = m.group(1)[0]
        target = prefix_map.get(prefix)
        if target:
            dst = ROOT / target / path.name
            mappings.append((path, dst))
        else:
            # fallback
            dst = ROOT / 'examples' / path.name
            mappings.append((path, dst))
    else:
        # other known files
        if path.name.startswith('comprehension') or 'comprehension' in path.name.lower():
            dst = ROOT / 'exercises' / 'comprehensions' / path.name
            mappings.append((path, dst))
        elif path.name in ('py_notes.txt',):
            dst = ROOT / 'docs' / path.name
            mappings.append((path, dst))
        else:
            # leave other files in place
            pass

# Create target dirs and move
for src, dst in mappings:
    try:
        dst_parent = dst.parent
        dst_parent.mkdir(parents=True, exist_ok=True)
        if src.is_dir():
            # move entire directory
            if dst.exists():
                print(f"Target {dst} already exists; merging {src} into it")
                for child in src.iterdir():
                    target_child = dst / child.name
                    print(f"  moving {child} -> {target_child}")
                    shutil.move(str(child), str(target_child))
                # optionally remove empty src dir
                try:
                    src.rmdir()
                except Exception:
                    pass
            else:
                shutil.move(str(src), str(dst))
            print(f"Moved dir {src} -> {dst}")
        else:
            target = dst
            if target.exists():
                print(f"Target file {target} exists; skipping {src}")
                continue
            shutil.move(str(src), str(target))
            print(f"Moved file {src} -> {target}")
    except Exception as e:
        print('Failed to move', src, '->', dst, e)

print('Reorganization complete. Please review moved files and update imports if needed.')
