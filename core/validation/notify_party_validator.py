class NotifyPartyValidator:

    def validate(self, invoice, bl):

        inv = getattr(invoice, "notify_party", None)
        bol = getattr(bl, "notify_party", None)

        if not inv or not bol:
            return []

        if inv.strip().upper() != bol.strip().upper():
            return ["NOTIFY_PARTY_MISMATCH"]

        return []
