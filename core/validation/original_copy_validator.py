class OriginalCopyValidator:

    def validate(self, mt700, invoice, bl, packing, insurance, coo):

        r=[]

        docs=[
            ("invoice",invoice),
            ("bill_of_lading",bl),
            ("packing_list",packing),
            ("insurance",insurance),
            ("certificate_of_origin",coo),
        ]

        for name,doc in docs:

            if doc is None:
                continue

            lc_org=getattr(mt700,f"{name}_originals",None)
            lc_cpy=getattr(mt700,f"{name}_copies",None)

            org=getattr(doc,"originals",None)
            cpy=getattr(doc,"copies",None)

            if lc_org is not None and org is not None:
                if int(lc_org)!=int(org):
                    r.append(f"{name.upper()}_ORIGINALS_MISMATCH")

            if lc_cpy is not None and cpy is not None:
                if int(lc_cpy)!=int(cpy):
                    r.append(f"{name.upper()}_COPIES_MISMATCH")

        return r
