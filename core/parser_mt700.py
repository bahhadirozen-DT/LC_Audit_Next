from models.mt700_model import MT700Model


def parse_mt700(text: str) -> MT700Model:
    """
    Basic SWIFT MT700 parser
    Converts raw MT700 text into MT700Model
    """

    data = {}

    lines = text.splitlines()

    i = 0

    while i < len(lines):
        line = lines[i].strip()

        if not line.startswith(":"):
            i += 1
            continue

        try:
            tag, value = line.split(":", 2)[1:]
        except ValueError:
            i += 1
            continue

        field_name = f"field{tag}"

        if field_name == "field32B":
            currency = value[:3]
            amount = value[3:].replace(",", "")

            data[field_name] = {
                "currency": currency,
                "amount": float(amount)
            }

        elif field_name in ["field31C", "field31D"]:
            from datetime import date
            data[field_name] = date(
                2000 + int(value[:2]),
                int(value[2:4]),
                int(value[4:6])
            )

        elif field_name == "field46A":
            docs = []

            i += 1
            while i < len(lines) and lines[i].strip().startswith("+"):
                docs.append(lines[i].strip()[1:])
                i += 1

            data[field_name] = {
                "documents": docs
            }

            continue

        elif field_name in ["field50", "field59"]:
            data[field_name] = value

        elif hasattr(MT700Model, field_name):
            data[field_name] = value

        i += 1

    return MT700Model(
        document_type="MT700",
        document_name="Documentary Credit",
        source_file="sample_mt700.txt",
        raw_text=text,

        lc_number=data.get("field20"),
        applicant=data.get("field50"),
        beneficiary=data.get("field59"),

        currency=data.get("field32B", {}).get("currency"),
        amount=data.get("field32B", {}).get("amount"),

        expiry_date=data.get("field31D"),

        required_documents=data.get("field46A", {}).get("documents", []),

        **{k:v for k,v in data.items() if k not in ["field50", "field59"]}
    )

