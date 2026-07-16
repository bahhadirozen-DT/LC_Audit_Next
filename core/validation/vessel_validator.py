class VesselValidator:

    def validate(self, invoice, bl):

        inv = getattr(invoice, "vessel", None)
        bol = getattr(bl, "vessel", None)

        if not inv or not bol:
            return []

        if inv.strip().upper() != bol.strip().upper():
            return ["VESSEL_MISMATCH"]

        return []
