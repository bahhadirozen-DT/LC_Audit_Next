import re

class PackageValidator:

    def _num(self, x):
        if not x:
            return None
        m = re.search(r'(\d+)', str(x))
        return int(m.group(1)) if m else None

    def validate(self, invoice, packing, bl):

        inv = self._num(getattr(invoice, "quantity", None))
        pl = self._num(getattr(packing, "total_packages", None))
        bol = self._num(getattr(bl, "packages", None))

        values = [v for v in (inv, pl, bol) if v is not None]

        if len(values) < 2:
            return []

        if len(set(values)) != 1:
            return ["PACKAGE_COUNT_MISMATCH"]

        return []
