import re

class AmountValidator:

    def _value(self, x):
        if not x:
            return None

        s = str(x).replace(",", "")
        m = re.search(r'([0-9]+(?:\.[0-9]+)?)', s)

        return float(m.group(1)) if m else None

    def validate(self, mt700, invoice):

        lc = self._value(getattr(mt700, "amount", None))
        inv = self._value(getattr(invoice, "amount", None))

        if lc is None or inv is None:
            return []

        if abs(lc - inv) > 0.01:
            return ["AMOUNT_MISMATCH"]

        return []
