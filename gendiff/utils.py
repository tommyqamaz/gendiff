import json
import yaml
from yaml import Loader


def get_file(path1, path2, mode="auto"):
    if mode == "auto":
        mode = path1.split(".")[-1]
    if mode == "json":
        file1 = json.load(open(path1))
        file2 = json.load(open(path2))
    elif mode in ["yaml", "yml"]:
        file1 = yaml.load(open(path1), Loader)
        file2 = yaml.load(open(path2), Loader)
    return file1, file2
