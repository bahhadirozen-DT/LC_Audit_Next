import re

from models.mt700_model import MT700Model


def _find(pattern, text):

    m = re.search(
        pattern,
        text,
        re.IGNORECASE | re.MULTILINE | re.DOTALL,
    )

    if m:
        return m.group(1).strip()

    return None


def parse_mt700(text: str):

    model = MT700Model(
        document_type="MT700",
        document_name="Documentary Credit",
        source_file="unknown",
        raw_text=text
    )

    model.raw_text = text

    # -----------------------------
    # SWIFT FORMAT
    # -----------------------------

    model.field20 = _find(r":20:(.+)", text)
    model.field31D = _find(r":31D:(.+)", text)
    model.field32B = _find(r":32B:([A-Z]{3}\s*[\d,\.]+)", text)
    model.field40A = _find(r":40A:(.+)", text)

    model.field50 = _find(r":50:([\s\S]*?)(?=\n:|\Z)", text)
    model.field59 = _find(r":59:([\s\S]*?)(?=\n:|\Z)", text)

    # -----------------------------
    # PDF FORMAT
    # -----------------------------

    if model.field20 is None:
        model.field20 = _find(r"FIELD\s*20\s*:\s*([^\n\r]+)", text)

    if model.field31D is None:
        model.field31D = _find(r"FIELD\s*31D\s*:\s*([^\n\r]+)", text)

    if model.field32B is None:
        model.field32B = _find(
            r"FIELD\s*32B\s*:\s*([^\n\r]+)",
            text,
        )

    if model.field40A is None:
        model.field40A = _find(
            r"FIELD\s*40A\s*:\s*([^\n\r]+)",
            text,
        )

    model.applicant = _find(
        r"Applicant.*?:\s*(.+?)(?=\n\s*\n|\nBeneficiary|\nPort)",
        text,
    )

    model.beneficiary = _find(
        r"Beneficiary.*?:\s*(.+?)(?=\n\s*\n|\nPort)",
        text,
    )

    model.issuing_bank = _find(
        r"Sender.*?:\s*(.+?)(?=\n\s*\n|\nApplicant)",
        text,
    )

    model.currency = None
    model.amount = None

    value = model.field32B

    if value:

        m = re.search(
            r"([A-Z]{3})\s*([\d\.,]+)",
            value,
        )

        if m:

            model.currency = m.group(1)

            amt = (
                m.group(2)
                .replace(".", "")
                .replace(",", ".")
            )

            try:
                model.amount = float(amt)
            except:
                pass

    model.lc_number = model.field20

    return model
