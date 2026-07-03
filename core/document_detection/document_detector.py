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
            ":32B:",
            ":40A:",
            ":45A:",
            ":46A:",
            "FIELD 20",
            "FIELD 27",
            "FIELD 31C",
            "FIELD 31D",
            "FIELD 32B",
            "FIELD 40A",
            "FIELD 45A",
            "FIELD 46A",
            "DOCUMENTARY CREDIT",
            "APPLICANT",
            "BENEFICIARY",
            "ISSUING BANK"
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
            "PACKING LIST NO",
            "PACKAGE DETAILS",
            "TOTAL PACKAGES",
            "PALLET NO",
            "PALLETS",
            "MARKS & NUMBERS",
            "CBM",
            "GROSS KG",
            "NET KG",
            "GROSS WEIGHT",
            "NET WEIGHT",
            "C/NO",
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
            "CERTIFICATE NO",
            "COUNTRY OF ORIGIN",
            "COUNTRY OF DESTINATION",
            "CHAMBER OF COMMERCE",
            "EXPORTER",
            "CONSIGNEE"
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
