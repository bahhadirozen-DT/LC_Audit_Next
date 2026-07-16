class InsuranceClauseValidator:

    def validate(self, mt700, insurance):

        lc = getattr(mt700, "insurance_clause", None)
        ic = getattr(insurance, "insurance_clause", None)

        if not lc or not ic:
            return []

        if lc.strip().upper() != ic.strip().upper():
            return ["INSURANCE_CLAUSE_MISMATCH"]

        return []
