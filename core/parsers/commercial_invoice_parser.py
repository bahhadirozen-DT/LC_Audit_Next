import re

from models.commercial_invoice_model import CommercialInvoiceModel


def parse_commercial_invoice(text: str):

    model = CommercialInvoiceModel()

    patterns = {
        "invoice_number": r"Invoice\s*No[:\s]+(.+)",
        "invoice_date": r"Date[:\s]+(.+)",
        "seller": r"Seller[:\s]+(.+)",
        "buyer": r"Buyer[:\s]+(.+)",
        "currency": r"Currency[:\s]+([A-Z]{3})",
        "total_amount": r"Total[:\s]+([\d\.,]+)",
        "incoterm": r"Incoterm[:\s]+(.+)"
    }

    for field, pattern in patterns.items():

        m = re.search(pattern, text, re.IGNORECASE)

        if not m:
            continue

        value = m.group(1).strip()

        if field == "total_amount":
            value = float(value.replace(",", ""))

        setattr(model, field, value)

    return model
