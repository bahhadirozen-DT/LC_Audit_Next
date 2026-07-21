import re

from models.certificate_of_origin_model import CertificateOfOriginModel


def g(pattern, text):
    m = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
    return m.group(1).strip() if m else None


def parse_certificate_of_origin(text: str):

    model = CertificateOfOriginModel()

    model.certificate_number = g(
        r"Certificate\s*(?:No|Number)?[:\s]*([A-Z0-9\-\/]+)",
        text,
    )

    model.exporter = g(
        r"Exporter[:\s]*(.+)",
        text,
    )

    model.consignee = g(
        r"(?:Consignee|Importer)[:\s]*(.+)",
        text,
    )

    model.country_of_origin = g(
        r"(?:Country of Origin|Goods Origin)[:\s]*(.+)",
        text,
    )

    model.country_of_destination = g(
        r"Country of Destination[:\s]*(.+)",
        text,
    )

    model.goods_description = g(
        r"Description[:\s]*(.+)",
        text,
    )

    model.signature = g(
        r"Signature[:\s]*(.+)",
        text,
    )

    model.chamber = g(
        r"Chamber.*?[:\s]*(.+)",
        text,
    )

    model.legalized = g(
        r"Legalized[:\s]*(.+)",
        text,
    )

    model.raw_text = text

    if not hasattr(model, "originals"):
        model.originals = None

    if not hasattr(model, "copies"):
        model.copies = None

    if not hasattr(model, "shipment_date"):
        model.shipment_date = None

    return model
