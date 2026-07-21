class DocumentDetector:

    def detect(self, text: str):

        t = text.upper()

        # -----------------------------------------------------
        # SWIFT MT700 shortcut
        # -----------------------------------------------------
        if ":20:" in t and ":27:" in t and ":31D:" in t:
            return {
                "document_type": "MT700",
                "confidence": 100,
                "scores": {"MT700": 100},
            }

        lines = [x.strip() for x in t.splitlines() if x.strip()]
        first = "\n".join(lines[:15])

        headers = [
            ("PACKING_LIST", "PACKING LIST"),
            ("COMMERCIAL_INVOICE", "COMMERCIAL INVOICE"),
            ("BILL_OF_LADING", "BILL OF LADING"),
            ("CERTIFICATE_OF_ORIGIN", "CERTIFICATE OF ORIGIN"),
            ("INSURANCE_CERTIFICATE", "INSURANCE CERTIFICATE"),
        ]

        for doc_type, header in headers:
            if header in first:
                return {
                    "document_type": doc_type,
                    "confidence": 100,
                    "scores": {doc_type: 100},
                }

        return {
            "document_type": "UNKNOWN",
            "confidence": 0,
            "scores": {},
        }
