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

            if left is None or right is None:
                status = "UNKNOWN"
            elif str(left).strip().upper() == str(right).strip().upper():
                status = "PASS"
            else:
                status = "FAIL"

            results.append({
                "document": document,
                "check": check,
                "status": status,
                "mt700": left,
                "document_value": right
            })

        if invoice:

            add(
                "COMMERCIAL_INVOICE",
                "Applicant vs Buyer",
                mt700.applicant,
                invoice.buyer
            )

            add(
                "COMMERCIAL_INVOICE",
                "Beneficiary vs Seller",
                mt700.beneficiary,
                invoice.seller
            )

            add(
                "COMMERCIAL_INVOICE",
                "Currency",
                mt700.currency,
                invoice.currency
            )

            add(
                "COMMERCIAL_INVOICE",
                "Amount",
                mt700.amount,
                invoice.total_amount
            )

        if packing:

            add(
                "PACKING_LIST",
                "Seller",
                mt700.beneficiary,
                getattr(packing, "exporter", None)
            )

            add(
                "PACKING_LIST",
                "Goods Description",
                None,
                getattr(packing, "goods_description", None)
            )

        if bl:

            add(
                "BILL_OF_LADING",
                "Shipper",
                mt700.beneficiary,
                bl.shipper
            )

            add(
                "BILL_OF_LADING",
                "Consignee",
                mt700.applicant,
                bl.consignee
            )

            add(
                "BILL_OF_LADING",
                "Port of Loading",
                getattr(mt700, "field44E", None),
                bl.port_of_loading
            )

            add(
                "BILL_OF_LADING",
                "Port of Discharge",
                getattr(mt700, "field44F", None),
                bl.port_of_discharge
            )

        if co:

            add(
                "CERTIFICATE_OF_ORIGIN",
                "Exporter",
                mt700.beneficiary,
                co.exporter
            )

            add(
                "CERTIFICATE_OF_ORIGIN",
                "Consignee",
                mt700.applicant,
                co.consignee
            )

            add(
                "CERTIFICATE_OF_ORIGIN",
                "Country of Origin",
                None,
                co.country_of_origin
            )

        if insurance:

            add(
                "INSURANCE_CERTIFICATE",
                "Beneficiary",
                mt700.applicant,
                insurance.insured
            )

            add(
                "INSURANCE_CERTIFICATE",
                "Currency",
                mt700.currency,
                insurance.currency
            )

        return results
