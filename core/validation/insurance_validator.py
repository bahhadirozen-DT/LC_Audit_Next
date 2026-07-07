class InsuranceValidator:
    """
    Validate whether the insurance document type satisfies
    the MT700 Field 46A requirement.
    """

    def validate(self, requires_policy: bool,
                 requires_certificate: bool,
                 uploaded_policy: bool,
                 uploaded_certificate: bool):

        result = {
            "status": "PASS",
            "errors": []
        }

        if requires_policy and not uploaded_policy:
            result["status"] = "FAIL"
            result["errors"].append(
                "Insurance Policy required but not provided."
            )

        if requires_certificate and not uploaded_certificate:
            result["status"] = "FAIL"
            result["errors"].append(
                "Insurance Certificate required but not provided."
            )

        return result
