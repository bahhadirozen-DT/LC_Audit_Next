class RequiredDocumentsValidator:

    """
    Backward compatible validator.

    Eski kullanım:
        validate(required_docs, uploaded_docs)

    Yeni kullanım:
        validate(mt700, uploaded_models)
    """

    def validate(self, a, b):

        # -------------------------
        # OLD TEST API
        # -------------------------
        if isinstance(a, list) and isinstance(b, list):

            required = {x.upper().strip() for x in a}
            uploaded = {x.upper().strip() for x in b}

            missing = sorted(required - uploaded)
            unexpected = sorted(uploaded - required)
            matched = sorted(required & uploaded)

            return {
                "status": "PASS" if not missing else "FAIL",
                "missing": missing,
                "unexpected": unexpected,
                "matched": matched,
            }

        # -------------------------
        # NEW ENGINE API
        # -------------------------

        mt700 = a
        uploaded_models = b

        required = {
            d.upper().strip()
            for d in getattr(mt700, "required_documents", [])
            if d
        }

        mapping = {
            "COMMERCIAL_INVOICE": "COMMERCIAL INVOICE",
            "PACKING_LIST": "PACKING LIST",
            "BILL_OF_LADING": "BILL OF LADING",
            "CERTIFICATE_OF_ORIGIN": "CERTIFICATE OF ORIGIN",
            "INSURANCE_CERTIFICATE": "INSURANCE CERTIFICATE",
        }

        uploaded = set()

        for doc in uploaded_models:

            t = getattr(doc, "document_type", "")

            if t in mapping:
                uploaded.add(mapping[t])

        missing = sorted(required - uploaded)

        if missing:
            return [
                "MISSING_DOCUMENTS: " + ", ".join(missing)
            ]

        return []
