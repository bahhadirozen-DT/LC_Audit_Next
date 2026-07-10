import re


STOPWORDS = {
    "THE",
    "OF",
    "AND",
    "PACKAGES",
    "PACKAGE",
    "PALLET",
    "PALLETS",
}


def normalize(goods):

    if goods is None:
        return ""

    goods = goods.upper()

    goods = re.sub(r"[^A-Z0-9 ]", " ", goods)

    words = [
        w
        for w in goods.split()
        if w not in STOPWORDS
    ]

    return " ".join(words)
