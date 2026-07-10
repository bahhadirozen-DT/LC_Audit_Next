
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
    r15_port_discharge,
    r21_legalized_coo,
    r20_required_documents,
    r19_original_copy,
    r18_insurance_risk,
    r17_insurance,
    r16_notify_party,
    r14_port_loading,
    r13_transshipment,
    r12_partial_shipment,
    r11_latest_shipment,
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
            r11_latest_shipment.check(lc, invoice),
            r12_partial_shipment.check(lc, invoice),
            r13_transshipment.check(lc, invoice),
            r14_port_loading.check(lc, invoice),
            r15_port_discharge.check(lc, invoice),
            r16_notify_party.check(lc, invoice),
            r17_insurance.check(lc, invoice),
            r18_insurance_risk.check(lc, invoice),
            r19_original_copy.check(lc, invoice),
            r20_required_documents.check(lc, invoice),
            r21_legalized_coo.check(lc, invoice),
        ]
