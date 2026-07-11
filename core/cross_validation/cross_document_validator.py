from core.validation.required_documents_validator import RequiredDocumentsValidator
from core.validation.original_copy_validator import OriginalCopyValidator
from core.validation.insurance_validator import InsuranceValidator
from core.validation.legalized_coo_validator import LegalizedCOOValidator

from core.validation.amount_validator import AmountValidator
from core.validation.applicant_validator import ApplicantValidator
from core.validation.shipper_validator import ShipperValidator
from core.validation.consignee_validator import ConsigneeValidator
from core.validation.goods_validator import GoodsValidator


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

        return results
