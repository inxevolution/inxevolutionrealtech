"""Allow execution as a module with python -m inxevolution_realtech."""

from .cli import main

if __name__ == "__main__":
    raise SystemExit(main())
