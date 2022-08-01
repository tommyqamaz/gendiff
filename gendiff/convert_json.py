import json
from re import L
import yaml
import argparse


def load_json(path: str) -> dict:
    return json.load(open(path))


def convert_to_yaml(dict_: dict, path_json: str):
    yaml.dump(dict_, open(path_json, "w"))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path_json")
    parser.add_argument("path_yaml")
    args = parser.parse_args()
    res = load_json(args.path_json)
    convert_to_yaml(res, args.path_yaml)


if __name__ == "__main__":
    main()
