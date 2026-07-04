class CrossDocumentAudit:

    def compare(
        self,
        mt700,
        invoice=None,
        packing=None,
        bl=None,
        co=None,
        insurance=None,
    ):

        results = []

        def add(document, check, left, right):

            left = "" if left is None else str(left).strip()
            right = "" if right is None else str(right).strip()

            if not left or not right:
                status = "UNKNOWN"
            elif left.upper() == right.upper():
                status = "PASS"
            else:
                status = "FAIL"

            results.append({
                "document": document,
                "check": check,
                "status": status,
                "mt700": left,
                "document_value": right,
            })

        if invoice:
            add(
                "COMMERCIAL_INVOICE",
                "Beneficiary",
                mt700.beneficiary,
                invoice.seller,
            )

            add(
                "COMMERCIAL_INVOICE",
                "Applicant",
                mt700.applicant,
                invoice.buyer,
            )

            add(
                "COMMERCIAL_INVOICE",
                "Currency",
                mt700.currency,
                invoice.currency,
            )

            add(
                "COMMERCIAL_INVOICE",
                "Amount",
                mt700.amount,
                invoice.total_amount,
            )

        if packing:
            add(
                "PACKING_LIST",
                "Goods Description",
                mt700.field45A.get("description") if isinstance(mt700.field45A, dict) else mt700.field45A,
                packing.goods_description,
            )

        if bl:
            add(
                "BILL_OF_LADING",
                "Port of Loading",
                mt700.field44A,
                bl.port_of_loading,
            )

            add(
                "BILL_OF_LADING",
                "Port of Discharge",
                mt700.field44B,
                bl.port_of_discharge,
            )

        if co:
            add(
                "CERTIFICATE_OF_ORIGIN",
                "Country Of Origin",
                None,
                co.country_of_origin,
            )

        if insurance:
            add(
                "INSURANCE_CERTIFICATE",
                "Insured",
                mt700.applicant,
                insurance.insured,
            )

        return results
