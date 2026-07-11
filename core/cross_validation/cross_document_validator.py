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

    def validate(self, documents):

        mt700 = None

        uploaded = []

        insurance_policy = False
        insurance_certificate = False

        legalized_uploaded = False

        originals = 0
        copies = 0

        for item in documents:

            model = item

            dtype = item.document_type

            if dtype == "MT700":
                mt700 = model
                continue

            uploaded.append(dtype)

            if getattr(model, "originals", None):
                originals += model.originals

            if getattr(model, "copies", None):
                copies += model.copies

            if dtype == "INSURANCE_CERTIFICATE":
                insurance_certificate = True

            if dtype == "INSURANCE_POLICY":
                insurance_policy = True

            if dtype == "CERTIFICATE_OF_ORIGIN":
                legalized_uploaded = bool(
                    getattr(model, "legalized", False)
                )

        if mt700 is None:
            return []

        results = []

        required_docs = [
            x["document"]
            for x in getattr(mt700, "required_document_specs", [])
        ]

        results.append(
            self.required.validate(
                required_docs,
                uploaded,
            )
        )

        for spec in getattr(mt700, "required_document_specs", []):

            if spec["document"] == "INSURANCE":

                results.append(
                    self.insurance.validate(
                        spec["policy"],
                        spec["certificate"],
                        insurance_policy,
                        insurance_certificate,
                    )
                )

            if spec["document"] == "CERTIFICATE_OF_ORIGIN":

                results.append(
                    self.legalized.validate(
                        spec["legalized"],
                        legalized_uploaded,
                    )
                )

            if spec["originals"] or spec["copies"]:

                results.append(
                    self.original.validate(
                        spec["originals"],
                        spec["copies"],
                        originals,
                        copies,
                    )
                )

        return results
