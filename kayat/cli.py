import argparse
import sys
from collections.abc import Sequence
from importlib.metadata import PackageNotFoundError, version


def create_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="kayat",
        description="A Python-first desktop GUI framework powered by HTML and CSS.",
    )
    parser.add_argument(
        "--version",
        action="store_true",
        help="show the installed Kayat version and exit",
    )
    return parser


def print_header() -> None:
    print("KAYAT")
    print("Python GUI Framework")


def main(argv: Sequence[str] | None = None) -> None:
    parser = create_parser()
    arguments = sys.argv[1:] if argv is None else argv
    options = parser.parse_args(arguments)
    if options.version:
        try:
            installed_version = version("kayat")
        except PackageNotFoundError:
            parser.error("could not determine the installed Kayat version")
        print(f"{parser.prog} {installed_version}")
        parser.exit()
    if not arguments:
        print_header()
