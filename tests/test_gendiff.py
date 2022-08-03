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
output_mode = "nested"

plain_cases = [
    (path1_json, path2_json, output_mode),
    (path1_yml, path2_yml, output_mode),
    (path1_json, path2_yml, output_mode),
    (path1_yml, path2_json, output_mode),
]

nexted_diff = read(get_fixture_path("diff_nested.txt")).rstrip().split("\n\n\n")
npath1 = get_fixture_path("nested_file1.json")
npath2 = get_fixture_path("nested_file2.json")
npath3 = get_fixture_path("nested_file1.yml")
npath4 = get_fixture_path("nested_file2.yml")
nested_cases = [(npath1, npath2, output_mode), (npath3, npath4, output_mode)]


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize("path1, path2, output_mode", plain_cases)
def test_plain(path1, path2, output_mode):
    result = generate_diff(path1, path2, output_mode)
    expected = plain_data[0]
    assert result == expected


@pytest.mark.parametrize("path1, path2, output_mode", nested_cases)
def test_nested(path1, path2, output_mode):
    result = generate_diff(path1, path2, output_mode)
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
        format="nested", first_file="first/path", second_file="second/path"
    )
