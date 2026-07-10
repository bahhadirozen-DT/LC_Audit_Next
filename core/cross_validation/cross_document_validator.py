from core.validation.required_documents_validator import RequiredDocumentsValidator
from core.validation.original_copy_validator import OriginalCopyValidator
from core.validation.insurance_validator import InsuranceValidator
from core.validation.legalized_coo_validator import LegalizedCOOValidator


class CrossDocumentValidator:

    def __init__(self):

        self.validators = [

            RequiredDocumentsValidator(),

            OriginalCopyValidator(),

            InsuranceValidator(),

            LegalizedCOOValidator(),

        ]

    def validate(self, lc, documents):

        results = []

        for validator in self.validators:

            if hasattr(validator, "validate"):

                try:

                    r = validator.validate(lc, documents)

                    if r:

                        if isinstance(r, list):

                            results.extend(r)

                        else:

                            results.append(r)

                except Exception as e:

                    results.append(
                        f"{validator.__class__.__name__.upper()} ERROR: {e}"
                    )

        return results
