import re

from models.insurance_certificate_model import InsuranceCertificateModel



def _find(pattern, text):
    m = re.search(pattern, text, re.IGNORECASE)
    return m.group(1).strip() if m else None

def parse_insurance_certificate(text):

    model = InsuranceCertificateModel()

    model.certificate_number = _find(
        r"Certificate\s*(?:No|Number)[:\s]+(.+)",
        text
    )

    model.policy_number = _find(
        r"Policy\s*(?:No|Number)[:\s]+(.+)",
        text
    )

    model.insured = _find(
        r"Insured[:\s]+(.+)",
        text
    )

    model.beneficiary = _find(
        r"Beneficiary[:\s]+(.+)",
        text
    )

    model.insurance_company = _find(
        r"Insurance\s*Company[:\s]+(.+)",
        text
    )

    model.insured_amount = _find(
        r"Insured\s*Amount[:\s]+(.+)",
        text
    )

    model.currency = _find(
        r"Currency[:\s]+([A-Z]{3})",
        text
    )

    # Benchmark compatibility
    model.insured_party = model.insured

    

    # --------------------------------------------------
    # Generic metadata
    # --------------------------------------------------


    model.insurance_clause=_find(
        r"Clauses?[:\\s]+([^\\n]+)",
        text
    )


    model.claims_payable=_find(
        r"Claims.*?:\\s*([^\\n]+)",
        text
    )


    model.endorsement=_find(
        r"Endorsement[:\\s]+([^\\n]+)",
        text
    )

    model.raw_text = text

    if not hasattr(model, "originals"):
        model.originals = None

    if not hasattr(model, "copies"):
        model.copies = None

    if not hasattr(model, "shipment_date"):
        model.shipment_date = None

    return model

