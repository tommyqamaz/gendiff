import json
import yaml
from yaml import Loader
from itertools import chain


def get_file(path: str) -> dict:
    """Read the file from path and returns dictionary."""
    mode = path.split(".")[-1]
    if mode == "json":
        return json.load(open(path))
    elif mode in ["yaml", "yml"]:
        return yaml.load(open(path), Loader)


def get_all_keys(*keys):
    """Transforms dict_keys to one list"""
    return sorted(set(list(chain.from_iterable(map(list, [*keys])))))


def _translate(value):
    """boolians and None's to pretty string representation"""
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return "null"
    return value


def get_diff_as_dict(file1, file2):
    """Returns the difference between two tree-like objects as a dictionary."""
    keys1 = file1.keys()
    keys2 = file2.keys()
    all_keys = get_all_keys(keys1, keys2)

    diff = {}

    for key in all_keys:
        empty = "89e604e4d0ab221519c1e9d97fac6e1819f5dfbc6ef4d0fade2e62ccd68780bf"
        output1 = _translate(file1.get(key, empty))
        output2 = _translate(file2.get(key, empty))
        if isinstance(output1, dict) and isinstance(output2, dict):
            output1 = get_diff_as_dict(output1, output2)
            diff.update({key: output1})
        elif output1 == output2:
            diff.update({key: output1})
        elif output1 == empty:
            diff.update({f"+{key}": output2})
        elif output2 == empty:
            diff.update({f"-{key}": output1})
        else:
            diff.update({f"-{key}": output1})
            diff.update({f"+{key}": output2})

    return diff
