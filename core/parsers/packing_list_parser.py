import re

from models.packing_list_model import PackingListModel


def find(pattern, text):
    m = re.search(pattern, text, re.I | re.S)
    

    # --------------------------------------------------
    # Generic metadata
    # --------------------------------------------------

    m.raw_text = text

    if not hasattr(m, "originals"):
        m.originals = None

    if not hasattr(m, "copies"):
        m.copies = None

    if not hasattr(m, "shipment_date"):
        m.shipment_date = None

    return m
.group(1).strip() if m else None


def parse_packing_list(text):

    m = PackingListModel()

    m.packing_list_number = find(
        r"Packing\s*List\s*No[:\s]+([^\n]+)",
        text
    )

    m.invoice_number = find(
        r"Commercial\s*Invoice\s*No[:\s]+([^\n]+)",
        text
    )

    m.exporter = find(
        r"Exporter[:\s]+(.*?)Importer:",
        text
    )

    m.importer = find(
        r"Importer[:\s]+(.*?)Marks",
        text
    )

    m.goods_description = find(
        r"Description[:\s]+(.*?)PACKAGE DETAILS",
        text
    )

    m.total_packages = find(
        r"Total\s*Packages[:\s]+([^\n]+)",
        text
    )

    gross = re.search(
        r"TOTAL.*?\|\s*[\d.,]+\s*MTRS\s*\|\s*([\d.,]+)",
        text,
        re.I | re.S
    )

    if gross:
        m.gross_weight = gross.group(1)

    net = re.search(
        r"TOTAL.*?\|\s*[\d.,]+\s*MTRS\s*\|\s*[\d.,]+\s*\|\s*([\d.,]+)",
        text,
        re.I | re.S
    )

    if net:
        m.net_weight = net.group(1)

    cbm = re.search(
        r"TOTAL.*?([\d.,]+\s*CBM)",
        text,
        re.I | re.S
    )

    if cbm:
        m.cbm = cbm.group(1)

    

    # --------------------------------------------------
    # Generic metadata
    # --------------------------------------------------

    m.raw_text = text

    if not hasattr(m, "originals"):
        m.originals = None

    if not hasattr(m, "copies"):
        m.copies = None

    if not hasattr(m, "shipment_date"):
        m.shipment_date = None

    return m

