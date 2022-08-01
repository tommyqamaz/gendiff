import json
import yaml
from yaml import Loader
from itertools import chain


def get_file(path: str, mode="auto") -> dict:
    """Read the file from path and returns dictionary."""
    if mode == "auto":
        mode = path.split(".")[-1]

    if mode == "json":
        return json.load(open(path))
    elif mode in ["yaml", "yml"]:
        return yaml.load(open(path), Loader)


def get_all_keys(*keys):
    """Transforms dict_keys to one list"""
    return sorted(set(list(chain.from_iterable(map(list, [*keys])))))


def get_diff_as_dict(file1, file2):
    """Returns the difference between two tree-like objects as a dictionary."""
    keys1 = file1.keys()
    keys2 = file2.keys()
    all_keys = get_all_keys(keys1, keys2)

    diff = {}

    for key in all_keys:
        output1 = file1.get(key, None)
        output2 = file2.get(key, None)
        if isinstance(output1, dict) and isinstance(output2, dict):
            output1 = get_diff_as_dict(output1, output2)
            diff.update({f"   {key}": output1})
        elif output1 == output2:
            diff.update({f"   {key}": output1})
        elif output1 is None:
            diff.update({f" + {key}": output2})
        elif output2 is None:
            diff.update({f" - {key}": output1})
        else:
            diff.update({f" - {key}": output1})
            diff.update({f" + {key}": output2})

    return diff
