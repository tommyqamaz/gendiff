def normilize(value):
    rejected = ["false", "true", "null"]
    if isinstance(value, dict):
        return "[complex value]"
    if isinstance(value, str):
        return f"'{value}'" if value not in rejected else value
    return value


def make_plain(value):
    res = []

    def walk(value, parent=None):
        if isinstance(value, dict):
            keys = value.keys()
            if "_added" in keys:
                if "_removed" in keys:
                    msg = (
                        f"Property '{parent}' was updated. "
                        f"From {normilize(value['_removed'])} "
                        f"to {normilize(value['_added'])}"
                    )
                    res.append(msg)
                else:
                    res.append(
                        f"Property '{parent}' was added with value: {normilize(value['_added'])}"
                    )
            elif "_removed" in keys:
                res.append(f"Property '{parent}' was removed")
            elif "_no_changes" in keys:
                pass
            else:
                for key, val in value.items():
                    if parent is None:
                        walk(val, str(key))
                    else:
                        walk(val, ".".join([str(parent), str(key)]))
        else:
            return

    walk(value)

    return "\n".join(res)
