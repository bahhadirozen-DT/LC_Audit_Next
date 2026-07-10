import re
from difflib import SequenceMatcher


def normalize(text):
    if text is None:
        return ""

    text = str(text).upper()

    text = text.replace("&", " AND ")

    text = re.sub(r"[.,;:/()\-_]", " ", text)

    text = re.sub(r"\s+", " ", text).strip()

    return text


def similarity(a, b):

    a = normalize(a)
    b = normalize(b)

    if not a and not b:
        return 100.0

    return round(
        SequenceMatcher(None, a, b).ratio() * 100,
        2,
    )


def equal(a, b, threshold=90):
    return similarity(a, b) >= threshold
