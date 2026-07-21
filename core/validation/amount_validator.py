import re


class AmountValidator:

    TOLERANCE = 0.01

    def _value(self, value):

        if value is None:
            return None

        s = str(value).replace(",", "")

        m = re.search(r"([0-9]+(?:\.[0-9]+)?)", s)

        if not m:
            return None

        return float(m.group(1))

    def validate(self, mt700, invoice):

        reserves = []

        lc_currency = getattr(mt700, "currency", None)
        inv_currency = getattr(invoice, "currency", None)

        if lc_currency and inv_currency:
            if str(lc_currency).upper() != str(inv_currency).upper():
                reserves.append("CURRENCY_MISMATCH")

        lc_amount = self._value(getattr(mt700, "amount", None))
        inv_amount = self._value(getattr(invoice, "amount", None))

        if lc_amount is None or inv_amount is None:
            return reserves

        if abs(lc_amount - inv_amount) > self.TOLERANCE:
            reserves.append("AMOUNT_MISMATCH")

        return reserves
