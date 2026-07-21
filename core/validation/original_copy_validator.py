class OriginalCopyValidator:

    def validate(self, *args):

        # --------------------------------------------------
        # Legacy unit tests (4 args)
        # --------------------------------------------------
        if len(args) == 4:

            req_originals, originals, req_copies, copies = args

            if originals != req_originals:
                return {
                    "status": "FAIL",
                    "reserve": "ORIGINALS_MISMATCH"
                }

            if copies < req_copies:
                return {
                    "status": "FAIL",
                    "reserve": "COPIES_MISMATCH"
                }

            return {
                "status": "PASS"
            }

        # --------------------------------------------------
        # Audit Engine (6 args)
        # --------------------------------------------------
        if len(args) == 6:

            lc, invoice, packing, bl, insurance, coo = args

            reserves = []

            for doc in (invoice, packing, bl, insurance, coo):

                if doc is None:
                    continue

                # gerçek kontrol daha sonra yazılacak

            return reserves

        raise TypeError("Unsupported validate() signature")
