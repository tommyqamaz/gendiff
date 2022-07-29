from gendiff import __version__
import pytest
from gendiff.scripts.gendiff import generate_diff


def test_version():
    assert __version__ == "0.1.0"


def test_gendiff():
    result = generate_diff("tests/fixtures/file1.json", "tests/fixtures/file2.json")
    expected = " - follow: False\n   host: hexlet.io\n - proxy: 123.234.53.22\n - timeout: 50\n + timeout: 20\n + verbose: True"
    assert result == expected


def test_cli():
    pass
