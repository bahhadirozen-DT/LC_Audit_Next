import difflib
import re


def normalize(text: str) -> str:
    if text is None:
        return ""

    text = text.upper()

    text = re.sub(r'[^A-Z0-9 ]', ' ', text)
    text = re.sub(r'\s+', ' ', text)

    return text.strip()


def similarity(a: str, b: str) -> float:
    a = normalize(a)
    b = normalize(b)

    if not a and not b:
        return 100.0

    return round(
        difflib.SequenceMatcher(None, a, b).ratio() * 100,
        2
    )
