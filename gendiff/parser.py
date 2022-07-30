import argparse


def get_parser():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument(
        "-f",
        "--format",
        help="set format of output",
        choices=["json", "yaml", "auto"],
        default="auto",
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    return parser
