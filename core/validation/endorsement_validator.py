class EndorsementValidator:

    def validate(self, mt700, insurance):

        lc = getattr(mt700, "endorsement", None)
        ins = getattr(insurance, "endorsement", None)

        if not lc or not ins:
            return []

        if lc.strip().upper() != ins.strip().upper():
            return ["ENDORSEMENT_MISMATCH"]

        return []
