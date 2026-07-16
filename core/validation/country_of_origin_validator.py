class CountryOfOriginValidator:

    def validate(self, invoice, coo):

        inv = getattr(invoice, "country_of_origin", None)
        cert = getattr(coo, "country_of_origin", None)

        if not inv or not cert:
            return []

        if inv.strip().upper() != cert.strip().upper():
            return ["COUNTRY_OF_ORIGIN_MISMATCH"]

        return []
