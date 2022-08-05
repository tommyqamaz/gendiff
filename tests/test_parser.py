from argparse import Namespace
import pytest

from gendiff.parser import get_parser


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
        format="stylish", first_file="first/path", second_file="second/path"
    )
