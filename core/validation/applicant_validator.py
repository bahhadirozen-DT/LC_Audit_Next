class ApplicantValidator:
    def validate(self, mt700, invoice):
        if getattr(mt700, "applicant", None) != getattr(invoice, "applicant", None):
            return ["APPLICANT_MISMATCH"]
        return []
