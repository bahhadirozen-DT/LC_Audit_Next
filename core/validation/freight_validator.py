class FreightValidator:

    def validate(self, mt700, bl):

        lc=getattr(mt700,"freight",None)
        bol=getattr(bl,"freight",None)

        if not lc or not bol:
            return []

        if lc.strip().upper()!=bol.strip().upper():
            return ["FREIGHT_MISMATCH"]

        return []
