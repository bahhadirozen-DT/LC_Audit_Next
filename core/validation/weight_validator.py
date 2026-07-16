import re

class WeightValidator:

    def _num(self, x):
        if not x:
            return None

        s = str(x).replace(",", ".")
        m = re.search(r'([0-9]+(?:\.[0-9]+)?)', s)

        return float(m.group(1)) if m else None

    def validate(self, packing, bl):

        p = self._num(getattr(packing, "gross_weight", None))
        b = self._num(getattr(bl, "gross_weight", None))

        if p is None or b is None:
            return []

        if abs(p - b) > 0.01:
            return ["GROSS_WEIGHT_MISMATCH"]

        return []
