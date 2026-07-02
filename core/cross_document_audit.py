class CrossDocumentAudit:

    def compare(self, mt700, invoice):

        results = []

        checks = [

            (
                "Applicant vs Buyer",
                mt700.applicant,
                invoice.buyer
            ),

            (
                "Beneficiary vs Seller",
                mt700.beneficiary,
                invoice.seller
            ),

            (
                "Currency",
                mt700.currency,
                invoice.currency
            ),

            (
                "Amount",
                mt700.amount,
                invoice.total_amount
            )

        ]

        for name, left, right in checks:

            status = "PASS" if left == right else "FAIL"

            results.append({

                "check": name,

                "status": status,

                "mt700": left,

                "invoice": right

            })

        return results
