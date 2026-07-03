import re

from models.packing_list_model import PackingListModel


def _find(pattern, text):

    m = re.search(pattern, text, re.IGNORECASE)

    if m:
        return m.group(1).strip()

    return None


def parse_packing_list(text: str):

    model = PackingListModel()

    model.packing_list_no = _find(
        r"Packing\s*List\s*No[:\s]+(.+)",
        text
    )

    model.exporter = _find(
        r"Exporter[:\s]+(.+)",
        text
    )

    model.importer = _find(
        r"Importer[:\s]+(.+)",
        text
    )

    model.packages = _find(
        r"Packages?[:\s]+(.+)",
        text
    )

    model.gross_weight = _find(
        r"Gross\s*Weight[:\s]+(.+)",
        text
    )

    model.net_weight = _find(
        r"Net\s*Weight[:\s]+(.+)",
        text
    )

    model.goods_description = _find(
        r"Description\s*of\s*Goods[:\s]+(.+)",
        text
    )

    return model
