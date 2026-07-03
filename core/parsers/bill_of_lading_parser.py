import re

from models.bill_of_lading_model import BillOfLadingModel


def _find(pattern, text):

    m = re.search(pattern, text, re.IGNORECASE)

    if m:
        return m.group(1).strip()

    return None


def parse_bill_of_lading(text: str):

    model = BillOfLadingModel()

    model.bl_number = _find(r"B/L\s*No[:\s]+(.+)", text)
    model.shipper = _find(r"Shipper[:\s]+(.+)", text)
    model.consignee = _find(r"Consignee[:\s]+(.+)", text)
    model.notify_party = _find(r"Notify\s*Party[:\s]+(.+)", text)

    model.vessel = _find(r"Vessel[:\s]+(.+)", text)

    model.port_of_loading = _find(
        r"Port\s*of\s*Loading[:\s]+(.+)",
        text
    )

    model.port_of_discharge = _find(
        r"Port\s*of\s*Discharge[:\s]+(.+)",
        text
    )

    model.goods_description = _find(
        r"Description\s*of\s*Goods[:\s]+(.+)",
        text
    )

    model.packages = _find(
        r"Packages[:\s]+(.+)",
        text
    )

    model.gross_weight = _find(
        r"Gross\s*Weight[:\s]+(.+)",
        text
    )

    return model
