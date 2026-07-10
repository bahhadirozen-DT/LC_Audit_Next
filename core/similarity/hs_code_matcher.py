import re


def normalize(code):

    if code is None:
        return ""

    return re.sub(r"\D", "", str(code))


def match(a, b):

    a = normalize(a)
    b = normalize(b)

    return {
        "score": 100 if a == b else 0,
        "matched": a == b,
    }
