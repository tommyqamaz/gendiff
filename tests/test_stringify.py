import os

import pytest

from gendiff.stringify import stringify


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, "fixtures", file_name)


def read(file_path):
    with open(file_path, "r") as f:
        result = f.read()
    return result


primitives = {
    "string": "value",
    "boolean": True,
    "number": 5,
}

nested = {
    "string": "value",
    "boolean": True,
    "number": 5,
    "dict": {
        5: "number",
        None: "None",
        True: "boolean",
        "value": "string",
        "nested": {
            "boolean": True,
            "string": "value",
            "number": 5,
            None: "None",
        },
    },
}

cases = [
    ("|-", 1, 0),
    ("|-", 2, 1),
    (" ", 3, 2),
]


@pytest.mark.parametrize("value", primitives.values())
def test_primitives(value):
    assert stringify(value) == str(value)


# expected_data = {"nested": [], "plain": []}
plain_data = read(get_fixture_path("plain.txt")).rstrip().split("\n\n\n")
nested_data = read(get_fixture_path("nested.txt")).rstrip().split("\n\n\n")


@pytest.mark.parametrize("replacer,spases_count,case_index", cases)
def test_plain(replacer, spases_count, case_index):
    expected = nested_data[case_index]
    assert stringify(nested, replacer, spases_count) == expected


@pytest.mark.parametrize("replacer,spases_count,case_index", cases)
def test_nested(replacer, spases_count, case_index):
    expected = plain_data[case_index]
    assert stringify(primitives, replacer, spases_count) == expected


def test_default_values():
    assert stringify(primitives) == plain_data[3]
    assert stringify(primitives, " ") == plain_data[3]
    assert stringify(primitives, "...") == plain_data[4]
    assert stringify(nested) == nested_data[3]
    assert stringify(nested, " ") == nested_data[3]
    assert stringify(nested, "...") == nested_data[4]
