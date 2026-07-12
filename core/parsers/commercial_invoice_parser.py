import re

from models.commercial_invoice_model import CommercialInvoiceModel


def find(pattern, text):
    m = re.search(pattern, text, re.I | re.S)
    return m.group(1).strip() if m else None

def parse_commercial_invoice(text):

    m = CommercialInvoiceModel()

    m.invoice_number = find(r"Invoice\s*No[:\s]+([^\n]+)", text)

    m.invoice_date = find(r"Invoice\s*Date[:\s]+([^\n]+)", text)

    m.seller = find(
        r"Exporter[:\s]+(.*?)Importer:",
        text
    )

    m.buyer = find(
        r"Importer[:\s]+(.*?)Consignee:",
        text
    )

    money = re.search(
        r"Total\s*Amount[:\s]+([A-Z]{3})\s*([\d.,]+)",
        text,
        re.I
    )

    if money:
        m.currency = money.group(1)
        m.total_amount = float(
            money.group(2)
            .replace(".", "")
            .replace(",", ".")
        )

    m.incoterm = find(
        r"Terms\s*of\s*Delivery[:\s]+([^\n]+)",
        text
    )

    m.hs_code = find(
        r"HS\s*Code[:\s]+([^\n]+)",
        text
    )

    m.quantity = find(
        r"Quantity[:\s]+([^\n]+)",
        text
    )

    m.unit_price = find(
        r"Unit\s*Price[:\s]+([^\n]+)",
        text
    )

    o=find(r"In\s*(\d+)\s*original",text)
    if o:
        m.originals=int(o)

    c=find(r"and\s*(\d+)\s*cop",text)
    if c:
        m.copies=int(c)

    goods = find(
        r"Description\s*of\s*Goods[:\s]+(.*?)Quantity:",
        text
    )

    if goods:
        m.goods.append(goods)

    # -----------------------------
    # Benchmark compatibility
    # -----------------------------
    m.amount = getattr(m, "total_amount", None)

    m.applicant = getattr(m, "buyer", None)

    if getattr(m, "goods", None):
        m.goods_description = "\n".join(m.goods)
    else:
        m.goods_description = None

    

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

