import re

from models.bill_of_lading_model import BillOfLadingModel


def find(pattern, text):
    m = re.search(pattern, text, re.I | re.S)
    return m.group(1).strip() if m else None


def parse_bill_of_lading(text):

    m = BillOfLadingModel()

    m.raw_text = text
    m.originals = None
    m.copies = None
    m.shipment_date = None

    m.bl_number = find(
        r"(?:B/L|Bill of Lading)\s*No[:\s]+([^\n]+)",
        text,
    )

    m.shipper = find(
        r"Shipper[:\s]+(.*?)Consignee:",
        text,
    )

    m.consignee = find(
        r"Consignee[:\s]+(.*?)Notify",
        text,
    )

    
    m.shipment_date = find(
        r"Shipped\s*on\s*Board:\s*Date:\s*([^\n]+)",
        text,
    )

    m.notify_party = find(
        r"Notify\s*Party[:\s]+(.*?)Vessel",
        text,
    )
    )

    m.vessel = find(
        r"Vessel[:\s]+([^\n]+)",
        text,
    )

    m.port_of_loading = find(
        r"Port\s*of\s*Loading[:\s]+([^\n]+)",
        text,
    )

    m.port_of_discharge = find(
        r"Port\s*of\s*Discharge[:\s]+([^\n]+)",
        text,
    )

    m.goods_description = find(
        r"Description\s*of\s*Goods[:\s]+(.*?)Packages",
        text,
    )

    m.packages = find(
        r"Packages[:\s]+([^\n]+)",
        text,
    )

    m.gross_weight = find(
        r"Gross\s*Weight[:\s]+([^\n]+)",
        text,
    )

    return m
