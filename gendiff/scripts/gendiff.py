from gendiff import generate_diff, get_parser
import sys


def main():
    parser = get_parser()
    args = parser.parse_args(sys.argv[1:])
    res = generate_diff(args.first_file, args.second_file, args.format)
    print(res)


if __name__ == "__main__":
    main()
