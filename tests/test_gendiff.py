import pytest

from .test_stringify import get_fixture_path, read
from gendiff.scripts.gendiff import generate_diff
from gendiff import __version__


plain_data = read(get_fixture_path("diff_plain.txt")).rstrip().split("\n\n\n")
path1_json = get_fixture_path("file1.json")
path2_json = get_fixture_path("file2.json")
path1_yml = get_fixture_path("file1.yml")
path2_yml = get_fixture_path("file2.yml")
output_mode1 = "nested"

plain_cases = [
    (path1_json, path2_json, output_mode1),
    (path1_yml, path2_yml, output_mode1),
    (path1_json, path2_yml, output_mode1),
    (path1_yml, path2_json, output_mode1),
]

nexted_diff = read(get_fixture_path("diff_nested.txt")).rstrip().split("\n\n\n")
npath1 = get_fixture_path("nested_file1.json")
npath2 = get_fixture_path("nested_file2.json")
npath3 = get_fixture_path("nested_file1.yml")
npath4 = get_fixture_path("nested_file2.yml")
nested_cases = [(npath1, npath2, output_mode1), (npath3, npath4, output_mode1)]


plain_diff = read(get_fixture_path("plain_diff.txt")).rstrip().split("\n\n\n")
output_mode2 = "plain"
plain_diff_cases = [(npath1, npath2, output_mode2), (npath3, npath4, output_mode2)]


def test_version():
    assert __version__ == "0.1.0"


@pytest.mark.parametrize("path1, path2, output_mode1", plain_cases)
def test_plain(path1, path2, output_mode1):
    result = generate_diff(path1, path2, output_mode1)
    expected = plain_data[0]
    assert result == expected


@pytest.mark.parametrize("path1, path2, output_mode1", nested_cases)
def test_nested(path1, path2, output_mode1):
    result = generate_diff(path1, path2, output_mode1)
    expected = nexted_diff[0]
    assert result == expected


@pytest.mark.parametrize("path1, path2, output_mode2", plain_diff_cases)
def test_diff_plain(path1, path2, output_mode2):
    result = generate_diff(path1, path2, output_mode2)
    expected = plain_diff[0]
    assert result == expected


def test_json():
    import json

    path = "tests/fixtures/json.json"
    file = json.load(open(path))
    result = generate_diff(npath1, npath2, "json")
    assert len(result) == 1446  # fix later
    assert len(file) == 4
