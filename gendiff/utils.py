import json
import yaml
from yaml import Loader


def get_file(path, mode="auto"):
    if mode == "auto":
        mode = path.split(".")[-1]

    if mode == "json":
        return json.load(open(path))
    elif mode in ["yaml", "yml"]:
        return yaml.load(open(path), Loader)
