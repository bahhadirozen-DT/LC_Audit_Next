class DocumentDetector:

    def detect(self, text: str):

        t = text.upper()

        # =====================================================
        # STAGE 1
        # HEADLINE DETECTION
        # =====================================================

        lines = [x.strip() for x in t.splitlines() if x.strip()]
        first = "\n".join(lines[:15])

        headers = [
            ("MT700", "MT700"),
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
                    "scores": {doc_type: 100}
                }

        # =====================================================
        # STAGE 2
        # KEYWORD SCORING
        # =====================================================

        keywords = {

            "MT700": [
                ":20:",
                ":27:",
                ":31D:",
                ":32B:",
                ":40A:",
                ":45A:",
                ":46A:"
            ],

            "COMMERCIAL_INVOICE": [
                "INVOICE NO",
                "INVOICE DATE",
                "TOTAL AMOUNT",
                "EXPORTER",
                "IMPORTER",
                "TERMS OF DELIVERY",
                "PAYMENT TERMS"
            ],

            "PACKING_LIST": [
                "PACKING LIST NO",
                "PACKAGE DETAILS",
                "TOTAL PACKAGES",
                "PALLET NO",
                "CBM",
                "NET KG",
                "GROSS KG"
            ],

            "BILL_OF_LADING": [
                "B/L NO",
                "OCEAN BILL OF LADING",
                "ON BOARD",
                "FREIGHT PREPAID",
                "FREIGHT COLLECT",
                "PLACE OF RECEIPT",
                "CARRIER"
            ],

            "CERTIFICATE_OF_ORIGIN": [
                "CERTIFICATE NO",
                "CERTIFY THAT",
                "ISSUED BY",
                "CHAMBER OF COMMERCE"
            ],

            "INSURANCE_CERTIFICATE": [
                "POLICY NO",
                "INSURANCE COMPANY",
                "INSURED",
                "CLAIMS",
                "SUM INSURED"
            ]
        }

        scores = {}

        for doc, words in keywords.items():

            score = 0

            for w in words:
                if w in t:
                    score += 10

            scores[doc] = score

        best = max(scores, key=scores.get)

        return {
            "document_type": best,
            "confidence": scores[best],
            "scores": scores
        }
