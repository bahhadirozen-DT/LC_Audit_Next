import re

class InsuranceAmountValidator:

    def _num(self, x):
        if not x:
            return None

        s = str(x).replace(",", "")
        m = re.search(r'([0-9]+(?:\.[0-9]+)?)', s)

        return float(m.group(1)) if m else None

    def validate(self, invoice, insurance):

        inv = self._num(getattr(invoice, "amount", None))
        ins = self._num(getattr(insurance, "insured_amount", None))

        if inv is None or ins is None:
            return []

        if ins < inv * 1.10:
            return ["INSURANCE_AMOUNT_INSUFFICIENT"]

        return []
