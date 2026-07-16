from core.validation.endorsement_validator import EndorsementValidator
from core.validation.insurance_clause_validator import InsuranceClauseValidator
from core.validation.insurance_amount_validator import InsuranceAmountValidator
from core.validation.quantity_validator import QuantityValidator
from core.validation.country_of_origin_validator import CountryOfOriginValidator
from core.validation.vessel_validator import VesselValidator
from core.validation.weight_validator import WeightValidator
from core.validation.package_validator import PackageValidator
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
from core.validation.notify_party_validator import NotifyPartyValidator
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

        self.package = PackageValidator()
        self.weight = WeightValidator()
        self.notify = NotifyPartyValidator()
        self.vessel = VesselValidator()
        self.country = CountryOfOriginValidator()
        self.hs = HSCodeValidator()
        self.quantity = QuantityValidator()
        self.insurance_amount = InsuranceAmountValidator()
        self.insurance_clause = InsuranceClauseValidator()
        self.endorsement = EndorsementValidator()

        self.hs_code = HSCodeValidator()
        self.incoterm = IncotermValidator()
        self.port = PortValidator()
        self.freight = FreightValidator()
        self.notify_party = NotifyPartyValidator()
        self.original_copy = OriginalCopyValidator()


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


        if mt700 and bl:
            results += self.notify_party.validate(mt700, bl)


        results += self.original_copy.validate(
            mt700,
            invoice,
            bl,
            packing,
            insurance,
            coo,
        )

        

        if invoice and packing and bl:
            results += self.package.validate(invoice, packing, bl)
            results += self.weight.validate(packing, bl)
            results += self.notify.validate(invoice, bl)
            results += self.vessel.validate(invoice, bl)
            results += self.quantity.validate(invoice, packing, bl)

        if invoice and coo:
            results += self.country.validate(invoice, coo)

        if mt700 and invoice:
            results += self.hs.validate(mt700, invoice)

        if invoice and insurance:
            results += self.insurance_amount.validate(invoice, insurance)

        if mt700 and insurance:
            results += self.insurance_clause.validate(mt700, insurance)
            results += self.endorsement.validate(mt700, insurance)


        return results
