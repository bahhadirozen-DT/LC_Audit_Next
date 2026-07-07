class LegalizedCOOValidator:
    """
    Validate whether a legalized Certificate of Origin
    is provided when required by MT700 Field 46A.
    """

    def validate(self, requires_legalized: bool,
                 uploaded_legalized: bool):

        result = {
            "status": "PASS",
            "errors": []
        }

        if requires_legalized and not uploaded_legalized:
            result["status"] = "FAIL"
            result["errors"].append(
                "Legalized Certificate of Origin required."
            )

        return result
