from core.validation.required_documents_validator import RequiredDocumentsValidator
from core.validation.original_copy_validator import OriginalCopyValidator
from core.validation.insurance_validator import InsuranceValidator
from core.validation.legalized_coo_validator import LegalizedCOOValidator

from core.validation.amount_validator import AmountValidator
from core.validation.applicant_validator import ApplicantValidator
from core.validation.shipper_validator import ShipperValidator
from core.validation.consignee_validator import ConsigneeValidator
from core.validation.goods_validator import GoodsValidator
from core.validation.freight_validator import FreightValidator
from core.validation.port_validator import PortValidator
from core.validation.incoterm_validator import IncotermValidator
from core.validation.hs_code_validator import HSCodeValidator


class CrossDocumentValidator:

    def __init__(self):

        self.required = RequiredDocumentsValidator()
        self.original = OriginalCopyValidator()
        self.insurance = InsuranceValidator()
        self.legalized = LegalizedCOOValidator()

        self.amount = AmountValidator()
        self.applicant = ApplicantValidator()
        self.shipper = ShipperValidator()
        self.consignee = ConsigneeValidator()
        self.goods = GoodsValidator()

        self.hs_code = HSCodeValidator()
        self.incoterm = IncotermValidator()
        self.port = PortValidator()
        self.freight = FreightValidator()


    def validate(self, models):

        mt700 = None
        invoice = None
        bl = None
        packing = None
        insurance = None
        coo = None

        for m in models:

            t = getattr(m, "document_type", "")

            if t == "MT700":
                mt700 = m

            elif t == "COMMERCIAL_INVOICE":
                invoice = m

            elif t == "BILL_OF_LADING":
                bl = m

            elif t == "PACKING_LIST":
                packing = m

            elif t == "INSURANCE_CERTIFICATE":
                insurance = m

            elif t == "CERTIFICATE_OF_ORIGIN":
                coo = m

        results = []

        if mt700 and invoice:
            results += self.amount.validate(mt700, invoice)
            results += self.applicant.validate(mt700, invoice)

        if invoice and bl:
            results += self.shipper.validate(invoice, bl)
            results += self.consignee.validate(invoice, bl)

        if invoice and packing and bl:
            results += self.goods.validate(invoice, packing, bl)

        if mt700 and insurance:
            r = self.insurance.validate(
                True,
                True,
                False,
                getattr(insurance, "insured_party", None) is not None,
            )
            if r["status"] == "FAIL":
                results.append("INSURED_PARTY_MISMATCH")

        if mt700 and coo:
            r = self.legalized.validate(
                True,
                getattr(coo, "legalized", False),
            )
            if r["status"] == "FAIL":
                results.append("LEGALIZED_CERTIFICATE_OF_ORIGIN")


        if mt700 and bl:
            mt_date = getattr(mt700, "latest_shipment_date", None)
            bl_date = getattr(bl, "shipment_date", None)

            if mt_date and bl_date:
                try:
                    from datetime import datetime

                    mt_dt = datetime.strptime(mt_date.strip(), "%d.%m.%Y")
                    bl_dt = datetime.strptime(bl_date.strip(), "%d.%m.%Y")

                    if bl_dt > mt_dt:
                        results.append("LATEST_SHIPMENT_DATE")

                except Exception:
                    pass


        if mt700 and invoice:
            results += self.hs_code.validate(mt700, invoice)
            results += self.incoterm.validate(mt700, invoice)

        if mt700 and bl:
            results += self.port.validate(mt700, bl)
            results += self.freight.validate(mt700, bl)

        return results
