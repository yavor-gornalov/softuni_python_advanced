def make_bold(func):
    tag = "b"

    def wrapper(*args, **kwargs):
        return f"<{tag}>{func(*args)}</{tag}>"

    return wrapper


def make_italic(func):
    tag = "i"

    def wrapper(*args, **kwargs):
        return f"<{tag}>{func(*args)}</{tag}>"

    return wrapper


def make_underline(func):
    tag = "u"

    def wrapper(*args, **kwargs):
        return f"<{tag}>{func(*args)}</{tag}>"

    return wrapper