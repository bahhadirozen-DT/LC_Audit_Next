
from core.reserves import (
    r01_applicant,
    r02_beneficiary,
    r03_invoice_amount,
    r04_currency,
    r05_goods_description,
    r06_quantity,
    r07_unit_price,
    r08_hs_code,
    r09_packing,
    r10_shipment_date,
)


class ReserveEngine:

    def run(self, lc, invoice):
        return [
            r01_applicant.check(lc, invoice),
            r02_beneficiary.check(lc, invoice),
            r03_invoice_amount.check(lc, invoice),
            r04_currency.check(lc, invoice),
            r05_goods_description.check(lc, invoice),
                    r06_quantity.check(lc, invoice),
            r07_unit_price.check(lc, invoice),
            r08_hs_code.check(lc, invoice),
            r09_packing.check(lc, invoice),
            r10_shipment_date.check(lc, invoice),
        ]
