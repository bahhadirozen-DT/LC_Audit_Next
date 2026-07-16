class IncotermValidator:

    def validate(self, mt700, invoice):

        lc = getattr(mt700, "incoterm", None)
        inv = getattr(invoice, "incoterm", None)

        if not lc or not inv:
            return []

        if lc.strip().upper() != inv.strip().upper():
            return ["INCOTERM_MISMATCH"]

        return []
