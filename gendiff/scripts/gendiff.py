from ..parser import get_parser
from ..utils import get_file, get_diff_as_dict
from ..formatters.stringify import stringify
import sys


def generate_diff(path1: str, path2: str) -> str:
    """Calculates the difference between two files (they can be diffent formats)."""

    file1 = get_file(path1)
    file2 = get_file(path2)

    diff = get_diff_as_dict(file1, file2)
    result = stringify(diff, " ", 4)
    return result


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    res = generate_diff(args.first_file, args.second_file)
    print(res)


if __name__ == "__main__":
    main()
