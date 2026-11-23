"""Tests for the starter command-line interface."""

from __future__ import annotations

import unittest

from inxevolution_realtech import __version__
from inxevolution_realtech.cli import build_parser, main


class CliTests(unittest.TestCase):
    def test_version_is_defined(self) -> None:
        self.assertEqual(__version__, "0.1.0")

    def test_parser_accepts_empty_arguments(self) -> None:
        parser = build_parser()
        args = parser.parse_args([])
        self.assertIsNotNone(args)

    def test_main_returns_success(self) -> None:
        self.assertEqual(main(), 0)


if __name__ == "__main__":
    unittest.main()
