class NotifyPartyValidator:

    def validate(self, mt700, bl):

        lc = getattr(mt700, "notify_party", None)
        bol = getattr(bl, "notify_party", None)

        if not lc or not bol:
            return []

        if lc.strip().upper() != bol.strip().upper():
            return ["NOTIFY_PARTY_MISMATCH"]

        return []
