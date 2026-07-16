class PaymentTermsValidator:

    def validate(self, mt700, invoice):

        lc = getattr(mt700, "payment_terms", None)
        inv = getattr(invoice, "payment_terms", None)

        if not lc or not inv:
            return []

        if str(lc).strip().upper() != str(inv).strip().upper():
            return ["PAYMENT_TERMS_MISMATCH"]

        return []
