class OriginalCopyValidator:

    def validate(self, *args):

        # -----------------------------
        # Legacy tests
        # validate(inv_org, inv_copy,
        #          lc_org, lc_copy)
        # -----------------------------
        if len(args) == 4 and all(isinstance(x, (int, type(None))) for x in args):

            inv_org, inv_copy, lc_org, lc_copy = args

            r = []

            if inv_org != lc_org:
                r.append("ORIGINALS_MISMATCH")

            if inv_copy != lc_copy:
                r.append("COPIES_MISMATCH")

            return r

        # -----------------------------
        # New parser architecture
        # -----------------------------
        if len(args) == 5:

            invoice, packing, bl, insurance, coo = args

            r = []

            docs = [invoice, packing, bl, insurance, coo]

            for d in docs:

                if d is None:
                    continue

                o = getattr(d, "originals", None)
                c = getattr(d, "copies", None)

                if o is None or c is None:
                    continue

            return r

        return []
