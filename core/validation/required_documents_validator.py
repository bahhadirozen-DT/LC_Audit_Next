from typing import List


class RequiredDocumentsValidator:
    """
    Compare MT700 Field 46A requirements with uploaded documents.
    """

    def validate(self, required_documents: List[str], uploaded_documents: List[str]):

        required = {d.upper().strip() for d in required_documents}
        uploaded = {d.upper().strip() for d in uploaded_documents}

        missing = sorted(required - uploaded)
        unexpected = sorted(uploaded - required)
        matched = sorted(required & uploaded)

        return {
            "status": "PASS" if not missing else "FAIL",
            "missing": missing,
            "unexpected": unexpected,
            "matched": matched,
        }
