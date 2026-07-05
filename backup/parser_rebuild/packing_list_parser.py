import re

from models.packing_list_model import PackingListModel


def find(pattern, text):
    m = re.search(pattern, text, re.I | re.S)
    return m.group(1).strip() if m else None


def parse_packing_list(text):

    m = PackingListModel()

    m.raw_text = text
    m.originals = None
    m.copies = None
    m.shipment_date = None

    m.packing_list_number = find(
        r"Packing\s*List\s*No[:\s]+([^\n]+)",
        text,
    )

    m.invoice_number = find(
        r"Commercial\s*Invoice\s*No[:\s]+([^\n]+)",
        text,
    )

    m.exporter = find(
        r"Exporter[:\s]+(.*?)Importer:",
        text,
    )

    m.importer = find(
        r"Importer[:\s]+(.*?)Country",
        text,
    )

    goods = find(
        r"Description[:\s]+(.*?)Quantity",
        text,
    )

    if goods:
        m.goods_description = goods

    return m
