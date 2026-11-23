# In X Evolution Real Technology — Python 3

This directory is the isolated Python 3 workspace for In X Evolution Real Technology. It is independent from ../landing-page/ and ../docs/.

## Scope

The initial foundation is a small, dependency-light command-line application skeleton. It does not yet implement a business product, connect to production systems, process personal data, or make network requests.

## Requirements

- Python 3.10 or newer
- pip
- No runtime third-party dependencies

## Project layout

    python3/
    ├── README.md
    ├── pyproject.toml
    ├── .gitignore
    ├── src/
    │   └── inxevolution_realtech/
    │       ├── __init__.py
    │       ├── __main__.py
    │       └── cli.py
    └── tests/
        └── test_cli.py

## Run locally

From this directory:

    python -m venv .venv

Activate the environment:
- Linux/macOS: source .venv/bin/activate
- Windows PowerShell: .venv\Scripts\Activate.ps1

Install in editable mode:

    python -m pip install --upgrade pip
    python -m pip install -e .

Run the application:

    python -m inxevolution_realtech

Or use the installed command:

    inxevolution-realtech

Run tests:

    python -m unittest discover -s tests -v

## Engineering conventions

- Keep application code inside src/.
- Keep automated tests inside tests/.
- Prefer the Python standard library until a concrete requirement justifies a dependency.
- Keep secrets out of source control; use environment variables or an approved secret manager.
- Add type hints and docstrings to public interfaces.
- Validate inputs at system boundaries.
- Log operational events without exposing credentials or personal data.
- Document architecture and material technical choices in the repository's docs/ directory.

## Status and next decisions

This is a starter foundation, not a production application. The product use case, users, data classification, external integrations, deployment target and operational owner must be approved before adding domain functionality.
