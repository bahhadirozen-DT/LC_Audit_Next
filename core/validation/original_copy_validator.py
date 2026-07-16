class OriginalCopyValidator:

    def validate(self, *args):

        # Eski test desteği
        if len(args) == 4:
            req_originals, originals, req_copies, copies = args

            if originals != req_originals:
                return {
                    "status": "FAIL",
                    "reserve": "ORIGINALS_MISMATCH"
                }

            return {
                "status": "PASS"
            }

        # Yeni engine desteği
        if len(args) == 5:
            invoice, packing, bl, insurance, coo = args

            reserves = []

            docs = [invoice, packing, bl, insurance, coo]

            for d in docs:
                if d is None:
                    continue

                if getattr(d, "originals", None) is None:
                    continue

                # Buraya gerçek LC karşılaştırması daha sonra gelecek

            return reserves

        raise TypeError("Unsupported validate() signature")
