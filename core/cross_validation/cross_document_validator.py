from core.validation.required_documents_validator import RequiredDocumentsValidator
from core.validation.original_copy_validator import OriginalCopyValidator
from core.validation.insurance_validator import InsuranceValidator
from core.validation.legalized_coo_validator import LegalizedCOOValidator


class CrossDocumentValidator:
    """
    Central dispatcher for all cross-document validation.
    """

    def __init__(self):
        self.required_documents = RequiredDocumentsValidator()
        self.original_copy = OriginalCopyValidator()
        self.insurance = InsuranceValidator()
        self.legalized_coo = LegalizedCOOValidator()

    def validators(self):
        return {
            "required_documents": self.required_documents,
            "original_copy": self.original_copy,
            "insurance": self.insurance,
            "legalized_coo": self.legalized_coo,
        }
