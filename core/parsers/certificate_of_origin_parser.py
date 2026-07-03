import re

from models.certificate_of_origin_model import CertificateOfOriginModel


def _find(pattern, text):

    m = re.search(pattern, text, re.IGNORECASE)

    if m:
        return m.group(1).strip()

    return None


def parse_certificate_of_origin(text):

    model = CertificateOfOriginModel()

    model.certificate_number = _find(
        r"Certificate\s*(?:No|Number)[:\s]+(.+)",
        text
    )

    model.exporter = _find(
        r"Exporter[:\s]+(.+)",
        text
    )

    model.consignee = _find(
        r"Consignee[:\s]+(.+)",
        text
    )

    model.country_of_origin = _find(
        r"Country\s*of\s*Origin[:\s]+(.+)",
        text
    )

    model.country_of_destination = _find(
        r"Country\s*of\s*Destination[:\s]+(.+)",
        text
    )

    model.goods_description = _find(
        r"Description.*?Goods[:\s]+(.+)",
        text
    )

    return model
