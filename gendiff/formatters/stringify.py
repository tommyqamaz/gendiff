from typing import Any


def _replace_symbol(string, symbol, replacer):
    string = string.replace(replacer, "", 1).replace(
        f"{replacer}{symbol}", f"{symbol}{replacer}", 1
    )
    return string


def process_result(replacer, spaces_count, _lvl, key):
    temp = f"{replacer*spaces_count*_lvl}{key}: "
    if str(key).startswith("+"):
        temp = _replace_symbol(temp, "+", replacer)
    elif str(key).startswith("-"):
        temp = _replace_symbol(temp, "-", replacer)
    return temp


def stringify(value: Any, replacer=" ", spaces_count=4) -> str:
    """Converts dictionary with differences to pretty string representation"""

    def inner(value, replacer, spaces_count, _lvl=1):
        """_lvl - nesting level"""
        if isinstance(value, dict):
            result = "{\n"
            for key, val in value.items():
                result += process_result(replacer, spaces_count, _lvl, key)
                result += inner(val, replacer, spaces_count, _lvl + 1) + "\n"
            result += replacer * spaces_count * (_lvl - 1) + "}"
        else:
            result = str(value)
        return result

    return inner(value, replacer, spaces_count, _lvl=1)
