from gendiff import __version__
import pytest
from gendiff.scripts.gendiff import generate_diff, get_parser
from argparse import Namespace


def test_version():
    assert __version__ == "0.1.0"


def test_gendiff():
    result = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    expected = " - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True"
    assert result == expected


def test_parser():
    parser = get_parser()

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args(["-h"])
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 0

    with pytest.raises(SystemExit) as excinfo:
        parser.parse_args()
    assert excinfo.type == SystemExit
    assert excinfo.value.code == 2

    assert parser.parse_args(["first/path", "second/path"]) == Namespace(
        format=None, first_file="first/path", second_file="second/path"
    )
