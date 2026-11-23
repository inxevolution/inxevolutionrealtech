"""Command-line entry point for the Python foundation."""

from __future__ import annotations

import argparse


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line argument parser."""
    parser = argparse.ArgumentParser(
        prog="inxevolution-realtech",
        description="In X Evolution Real Technology — Python foundation.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 0.1.0",
    )
    return parser


def main() -> int:
    """Run the command-line application."""
    parser = build_parser()
    parser.parse_args()
    print("In X Evolution Real Technology — Python foundation ready.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
