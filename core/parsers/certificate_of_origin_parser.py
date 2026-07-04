import re

from models.certificate_of_origin_model import CertificateOfOriginModel


def g(pattern, text):
    m = re.search(pattern, text, re.I | re.M)
    return m.group(1).strip() if m else None


def parse_certificate_of_origin(text: str):

    m = CertificateOfOriginModel()

    m.certificate_number = g(
        r"^Certificate\s*(?:No|Number)?[:\s]*([A-Z0-9\-\/]+)$",
        text,
    )

    m.exporter = g(
        r"^Exporter:\s*(.+)$",
        text,
    )

    m.consignee = g(
        r"^(?:Consignee|Importer):\s*(.+)$",
        text,
    )

    m.country_of_origin = g(
        r"^(?:Country of Origin|Goods Origin):\s*(.+)$",
        text,
    )

    m.country_of_destination = g(
        r"^Country of Destination:\s*(.+)$",
        text,
    )

    m.goods_description = g(
        r"Description:\s*([\s\S]*?)\nSignature:",
        text,
    )

    return m
