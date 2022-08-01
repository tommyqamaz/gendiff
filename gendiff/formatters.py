from typing import Any


def stringify(value: Any, replacer=" ", spaces_count=1):
    """
    Converts any value to string representation.
    In [1]: plain
    Out[2]: {'string': 'value', 'boolean': True, 'number': 5}
    In [3]: stringify(plain, ' ', 3)
    Out[4]: '{\n   string: value\n   boolean: True\n   number: 5\n}'

    In [5]: print(_)
    {
       string: value
       boolean: True
       number: 5
    }
    """

    def inner(value, replacer, spaces_count, _lvl=1):
        """_lvl - nesting level"""
        if isinstance(value, dict):
            result = "{\n"
            for key, val in value.items():
                result += f"{replacer*spaces_count*_lvl}{key}: "
                result += inner(val, replacer, spaces_count, _lvl + 1) + "\n"
            result += replacer * spaces_count * (_lvl - 1) + "}"
        else:
            result = str(value)
        return result

    return inner(value, replacer, spaces_count, _lvl=1)
