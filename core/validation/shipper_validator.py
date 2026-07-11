class ShipperValidator:
    def validate(self, invoice, bl):
        if getattr(invoice, "shipper", None) != getattr(bl, "shipper", None):
            return ["SHIPPER_MISMATCH"]
        return []
