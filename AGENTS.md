# AGENTS.md

## Cursor Cloud specific instructions

This is a Python-based DSA (Data Structures and Algorithms) practice repository. There are no web services, databases, or application servers to run.

### Project structure

- `code/` — All algorithm solutions organized by topic (sliding-window, two-pointers, binary-search, etc.)
- `code/utils/test_runner.py` — Custom `TestCaseRunner` utility used by some solutions for inline test assertions
- `code/justfile` — Task runner recipes for linting, formatting, and git push
- `system-design/` — System design notes in Markdown
- `amazon/` — Amazon-specific practice problems

### Running solutions

Each `.py` file is a standalone script. Run any solution directly:
```
python3 code/<topic>/<file>.py
```

### Linting and formatting

From the `code/` directory:
```
just lint      # flake8 with --max-line-length=120
just format    # black with --line-length=120
```

Or run directly from anywhere:
```
flake8 code/ --exclude=venv/* --max-line-length=120
black code/ --exclude=venv/* --line-length=120 --check
```

### Notes

- `just` (command runner) must be installed system-wide; the update script handles `flake8` and `black` via pip.
- Python tools install to `~/.local/bin` — this directory must be on `PATH` (added to `~/.bashrc` during setup).
- There is no `requirements.txt` in the repo; the justfile references one but it does not exist. Dependencies are just `flake8` and `black`.
