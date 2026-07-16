import re

class QuantityValidator:

    def _num(self, s):
        if not s:
            return None
        m = re.search(r'([\d.,]+)', str(s))
        if not m:
            return None
        return float(m.group(1).replace(".", "").replace(",", "."))

    def validate(self, invoice, packing):

        q1 = self._num(getattr(invoice, "quantity", None))
        q2 = self._num(getattr(packing, "quantity", None))

        if q1 is None or q2 is None:
            return []

        if abs(q1 - q2) > 0.01:
            return ["QUANTITY_MISMATCH"]

        return []
