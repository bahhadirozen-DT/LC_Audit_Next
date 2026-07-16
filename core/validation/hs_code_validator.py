class HSCodeValidator:

    def validate(self, mt700, invoice):

        hs1 = getattr(mt700, "hs_code", None)
        hs2 = getattr(invoice, "hs_code", None)

        if not hs1 or not hs2:
            return []

        if str(hs1).strip() != str(hs2).strip():
            return ["HS_CODE_MISMATCH"]

        return []
