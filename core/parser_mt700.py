from models.mt700_model import MT700Model


def parse_mt700(text: str) -> MT700Model:
    """
    Basic SWIFT MT700 parser
    Converts raw MT700 text into MT700Model
    """

    data = {}

    lines = text.splitlines()

    for line in lines:
        line = line.strip()

        if not line.startswith(":"):
            continue

        try:
            tag, value = line.split(":", 2)[1:]
        except ValueError:
            continue

        field_name = f"field{tag}"

        if field_name == "field32B":
            currency = value[:3]
            amount = value[3:].replace(",", "")

            data[field_name] = {
                "currency": currency,
                "amount": float(amount)
            }

        elif field_name in ["field50", "field59"]:
            data[field_name] = value

        elif hasattr(MT700Model, field_name):
            data[field_name] = value

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

        **{k:v for k,v in data.items() if k not in ["field50", "field59"]}
    )

