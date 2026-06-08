# p_time

This repository contains learning examples and small exercises used for Python practice.

Structure (reorganized):

- `src/` - helper libraries and utilities (package code)
  - `src/utils/` - utility scripts (e.g., `clear`)
- `examples/` - lesson/example scripts grouped by topic
  - `examples/01_identifiers/` (identifiers & keywords)
  - `examples/02_datatypes/` (data type examples)
  - `examples/03_strings/` (string examples)
  - `examples/04_operators/`
  - `examples/05_io/`
  - `examples/06_control_flow/`
  - `examples/07_loops/`
  - `examples/08_patterns/`
  - `examples/09_string_ops/`
  - `examples/00_misc/`
- `exercises/` - small exercises and challenges
  - `exercises/comprehensions/`
- `apps/` - larger projects (e.g., `todo-expo`)
- `docs/` - notes and documentation
- `scripts/` - helper scripts (reorganization, maintenance)

How to apply the reorganization

Run the provided script to move files into the new layout (it will create target folders as needed):

```powershell
python scripts\reorganize.py
```

If you plan to push this to GitHub:

1. Initialize git: `git init`
2. Create a new repo on GitHub
3. Add remote and push

If you'd like, I can run the reorganization script now and update imports where needed.
