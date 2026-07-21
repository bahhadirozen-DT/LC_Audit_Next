class ApplicantValidator:

    def validate(self, mt700, invoice):

        reserves = []

        lc = getattr(mt700, "applicant", None)

        inv = (
            getattr(invoice, "seller", None)
            or getattr(invoice, "exporter", None)
            or getattr(invoice, "applicant", None)
        )

        if not lc or not inv:
            return reserves

        if lc.strip().upper() != inv.strip().upper():
            reserves.append("APPLICANT_MISMATCH")

        return reserves
