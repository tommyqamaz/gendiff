from .utils import get_file, get_diff_as_dict
from .formatters.stringify import stringify
from .formatters.make_plain import make_plain
from .formatters.jsonify import to_json


def generate_diff(path1: str, path2: str, output_mode: str) -> str:
    """Calculates the difference between two files (they can be diffent formats)."""

    file1 = get_file(path1)
    file2 = get_file(path2)

    diff = get_diff_as_dict(file1, file2, output_mode)
    modes = {"nested": stringify, "plain": make_plain, "json": to_json}
    result = modes[output_mode](diff)
    return result
