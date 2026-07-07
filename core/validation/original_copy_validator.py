class OriginalCopyValidator:
    """
    Validate required originals/copies against uploaded document metadata.
    """

    def validate(self, required_originals, required_copies,
                 uploaded_originals, uploaded_copies):

        result = {
            "status": "PASS",
            "errors": []
        }

        if required_originals is not None:
            if uploaded_originals is None or uploaded_originals < required_originals:
                result["status"] = "FAIL"
                result["errors"].append(
                    f"Originals required: {required_originals}, uploaded: {uploaded_originals}"
                )

        if required_copies is not None:
            if uploaded_copies is None or uploaded_copies < required_copies:
                result["status"] = "FAIL"
                result["errors"].append(
                    f"Copies required: {required_copies}, uploaded: {uploaded_copies}"
                )

        return result
