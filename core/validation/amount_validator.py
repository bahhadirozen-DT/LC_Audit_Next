class AmountValidator:
    def validate(self, mt700, invoice):
        if getattr(mt700, "amount", None) != getattr(invoice, "amount", None):
            return ["AMOUNT_MISMATCH"]
        return []
