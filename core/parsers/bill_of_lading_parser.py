import re

from models.bill_of_lading_model import BillOfLadingModel


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


def parse_bill_of_lading(text):

    m = BillOfLadingModel()

    m.bl_number = find(
        r"(?:B/L|Bill of Lading)\s*No[:\s]+([^\n]+)",
        text
    )

    m.shipper = find(
        r"Shipper[:\s]+(.*?)Consignee:",
        text
    )

    m.consignee = find(
        r"Consignee[:\s]+(.*?)Notify",
        text
    )

    m.notify_party = find(
        r"Notify\s*Party[:\s]+(.*?)Vessel",
        text
    )

    m.vessel = find(
        r"Vessel[:\s]+([^\n]+)",
        text
    )

    m.port_of_loading = find(
        r"Port\s*of\s*Loading[:\s]+([^\n]+)",
        text
    )

    m.port_of_discharge = find(
        r"Port\s*of\s*Discharge[:\s]+([^\n]+)",
        text
    )

    m.goods_description = find(
        r"Description\s*of\s*Goods[:\s]+(.*?)Packages",
        text
    )

    m.packages = find(
        r"Packages[:\s]+([^\n]+)",
        text
    )

    m.gross_weight = find(
        r"Gross\s*Weight[:\s]+([^\n]+)",
        text
    )

    

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

