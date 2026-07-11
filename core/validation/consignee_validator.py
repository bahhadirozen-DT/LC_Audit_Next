class ConsigneeValidator:
    def validate(self, invoice, bl):
        if getattr(invoice, "consignee", None) != getattr(bl, "consignee", None):
            return ["CONSIGNEE_MISMATCH"]
        return []
