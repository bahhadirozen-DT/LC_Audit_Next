from core.validation.required_documents_validator import RequiredDocumentsValidator
from core.validation.original_copy_validator import OriginalCopyValidator
from core.validation.insurance_validator import InsuranceValidator
from core.validation.legalized_coo_validator import LegalizedCOOValidator


class CrossDocumentValidator:

    def __init__(self):
        self.required_documents = RequiredDocumentsValidator()
        self.original_copy = OriginalCopyValidator()
        self.insurance = InsuranceValidator()
        self.legalized_coo = LegalizedCOOValidator()

    def validate(self, lc, documents):

        results = {}

        uploaded_types = [
            getattr(d, "document_type", "").upper()
            for d in documents
        ]

        results["required_documents"] = self.required_documents.validate(
            getattr(lc, "required_documents", []),
            uploaded_types,
        )

        results["original_copy"] = self.original_copy.validate(
            getattr(lc, "required_originals", None),
            getattr(lc, "required_copies", None),
            sum(getattr(d, "originals", 0) for d in documents),
            sum(getattr(d, "copies", 0) for d in documents),
        )

        results["insurance"] = self.insurance.validate(
            getattr(lc, "requires_insurance_policy", False),
            getattr(lc, "requires_insurance_certificate", False),
            any(getattr(d, "document_type", "") == "INSURANCE_POLICY" for d in documents),
            any(getattr(d, "document_type", "") == "INSURANCE_CERTIFICATE" for d in documents),
        )

        results["legalized_coo"] = self.legalized_coo.validate(
            getattr(lc, "requires_legalized_coo", False),
            any(getattr(d, "legalized", False) for d in documents),
        )

        return results
