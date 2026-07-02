import re


class DocumentDetector:

    def detect(self, text: str):

        t = text.upper()

        scores = {
            "MT700": 0,
            "COMMERCIAL_INVOICE": 0,
            "PACKING_LIST": 0,
            "BILL_OF_LADING": 0,
            "CERTIFICATE_OF_ORIGIN": 0,
            "INSURANCE_CERTIFICATE": 0,
        }

        # ---------- MT700 ----------

        mt_tags = [
            ":20:",
            ":27:",
            ":31C:",
            ":31D:",
            ":40A:",
            ":46A:"
        ]

        for tag in mt_tags:
            if tag in t:
                scores["MT700"] += 20

        # ---------- Commercial Invoice ----------

        invoice_words = [
            "INVOICE",
            "SELLER",
            "BUYER",
            "INCOTERM",
            "TOTAL"
        ]

        for w in invoice_words:
            if w in t:
                scores["COMMERCIAL_INVOICE"] += 20

        # ---------- Packing List ----------

        packing_words = [
            "PACKING LIST",
            "NET WEIGHT",
            "GROSS WEIGHT",
            "PACKAGE",
            "CARTON"
        ]

        for w in packing_words:
            if w in t:
                scores["PACKING_LIST"] += 20

        # ---------- Bill of Lading ----------

        bl_words = [
            "BILL OF LADING",
            "CONSIGNEE",
            "SHIPPER",
            "VESSEL",
            "PORT OF LOADING"
        ]

        for w in bl_words:
            if w in t:
                scores["BILL_OF_LADING"] += 20

        # ---------- Certificate of Origin ----------

        co_words = [
            "CERTIFICATE OF ORIGIN",
            "COUNTRY OF ORIGIN",
            "CHAMBER OF COMMERCE"
        ]

        for w in co_words:
            if w in t:
                scores["CERTIFICATE_OF_ORIGIN"] += 34

        # ---------- Insurance ----------

        insurance_words = [
            "INSURANCE CERTIFICATE",
            "INSURED",
            "CLAIMS",
            "POLICY"
        ]

        for w in insurance_words:
            if w in t:
                scores["INSURANCE_CERTIFICATE"] += 25

        best = max(scores, key=scores.get)

        return {
            "document_type": best,
            "confidence": scores[best],
            "scores": scores
        }
