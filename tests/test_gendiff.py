from argparse import Namespace
import pytest

from .test_stringify import get_fixture_path, read
from gendiff.scripts.gendiff import generate_diff
from gendiff.parser import get_parser
from gendiff import __version__


plain_data = read(get_fixture_path("diff_plain.txt")).rstrip().split("\n\n\n")
path1_json = get_fixture_path("file1.json")
path2_json = get_fixture_path("file2.json")
path1_yml = get_fixture_path("file1.yml")
path2_yml = get_fixture_path("file2.yml")

plain_cases = [
    (path1_json, path2_json),
    (path1_yml, path2_yml),
    (path1_json, path2_yml),
    (path1_yml, path2_json),
]

nexted_diff = read(get_fixture_path("example_nested.txt")).rstrip().split("\n\n\n")
npath1 = get_fixture_path("nested_file1.json")
npath2 = get_fixture_path("nested_file2.json")
nested_cases = [(npath1, npath2)]


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize("path1, path2", plain_cases)
def test_plain(path1, path2):
    result = generate_diff(path1, path2, mode="auto")
    expected = plain_data[0]
    assert result == expected


@pytest.mark.parametrize("path1, path2", nested_cases)
def test_nested(path1, path2):
    result = generate_diff(path1, path2, mode="auto")
    expected = nexted_diff[0]
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
        format="auto", first_file="first/path", second_file="second/path"
    )
