from datetime import date
from models.mt700_model import MT700Model


def parse_date(value):
    value = value.strip()

    if len(value) == 6 and value.isdigit():
        return date(
            2000 + int(value[0:2]),
            int(value[2:4]),
            int(value[4:6])
        )

    return value


def parse_mt700(text: str) -> MT700Model:
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


        field = f"field{tag}"


        if field == "field32B":
            data[field] = {
                "currency": value[:3],
                "amount": float(value[3:].replace(",", ""))
            }


        elif field in ["field31C", "field31D", "field44C"]:
            data[field] = parse_date(value)


        elif field == "field46A":

            docs = []

            i += 1

            while i < len(lines) and lines[i].strip().startswith("+"):
                docs.append(
                    lines[i].strip()[1:]
                )
                i += 1

            data[field] = {
                "documents": docs
            }

            continue


        elif field == "field71B":

            data[field] = [
                value
            ]


        elif hasattr(MT700Model, field):

            data[field] = value


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


        latest_shipment_date=data.get("field44C"),


        required_documents=data.get(
            "field46A",
            {}
        ).get(
            "documents",
            []
        ),


        **data

    )
