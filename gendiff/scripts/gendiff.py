import argparse
from itertools import chain
import sys
import json


def generate_diff(path1: str, path2: str):
    diff = {}

    file1 = json.load(open(path1))
    file2 = json.load(open(path2))

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


def get_parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("-f", "--format", help="set format of output", choices=["json"])
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    return parser


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    res = generate_diff(args.first_file, args.second_file)
    print(res)


if __name__ == "__main__":
    main()
