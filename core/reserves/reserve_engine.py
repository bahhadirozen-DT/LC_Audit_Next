from core.reserves import (
    r01_applicant,
    r02_beneficiary,
    r03_invoice_amount,
    r04_currency,
    r05_goods_description,
)

class ReserveEngine:

    def run(self, lc, invoice):
        return [
            r01_applicant.check(lc, invoice),
            r02_beneficiary.check(lc, invoice),
            r03_invoice_amount.check(lc, invoice),
            r04_currency.check(lc, invoice),
            r05_goods_description.check(lc, invoice),
        ]
