from ..parser import get_parser
from ..utils import get_file
from itertools import chain
import sys


def generate_diff(path1: str, path2: str, mode: str) -> str:
    diff = {}

    file1 = get_file(path1, mode)
    file2 = get_file(path2, mode)

    keys1 = file1.keys()
    keys2 = file2.keys()

    all_keys = sorted(set(list(chain.from_iterable(map(list, [keys1, keys2])))))
    diff = []
    for key in all_keys:
        output1 = file1.get(key, None)
        output2 = file2.get(key, None)
        if output1 == output2:
            diff.append(f"   {key}: {output1}")
        elif output1 is None:
            diff.append(f" + {key}: {output2}")
        elif output2 is None:
            diff.append(f" - {key}: {output1}")
        else:
            diff.append(f" - {key}: {output1}")
            diff.append(f" + {key}: {output2}")

    return "\n".join(diff)


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    res = generate_diff(args.first_file, args.second_file, args.format)
    print(res)


if __name__ == "__main__":
    main()
