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

        from core.utils.value_compare import ValueComparer

        rows=[]

        def val(obj,*names):
            if obj is None:
                return None
            for n in names:
                if hasattr(obj,n):
                    v=getattr(obj,n)
                    if v not in (None,"",[],{}):
                        return v
            return None

        def add(document,check,left,right):

            result=ValueComparer.compare(left,right)

            status=result["status"]
            reason=result["reason"]

            rows.append({
                "document":document,
                "check":check,
                "status":status,
                "mt700":left,
                 "document_value":right,
                "reason":reason
            })

        # ===========================
        # COMMERCIAL INVOICE
        # ===========================

        if invoice:

            add(
                "COMMERCIAL_INVOICE",
                "Applicant / Buyer",
                val(mt700,"applicant"),
                val(invoice,"buyer","importer")
            )

            add(
                "COMMERCIAL_INVOICE",
                "Beneficiary / Seller",
                val(mt700,"beneficiary"),
                val(invoice,"seller","exporter")
            )

            add(
                "COMMERCIAL_INVOICE",
                "Currency",
                val(mt700,"currency"),
                val(invoice,"currency")
            )

            add(
                "COMMERCIAL_INVOICE",
                "Amount",
                val(mt700,"amount"),
                val(invoice,"total_amount")
            )

        # ===========================
        # PACKING LIST
        # ===========================

        if packing:

            add(
                "PACKING_LIST",
                "Goods Description",
                val(invoice,"goods"),
                val(packing,"goods_description")
            )

            add(
                "PACKING_LIST",
                "Gross Weight",
                val(invoice,"gross_weight"),
                val(packing,"gross_weight")
            )

            add(
                "PACKING_LIST",
                "Packages",
                val(invoice,"packages"),
                val(packing,"packages")
            )

        # ===========================
        # BILL OF LADING
        # ===========================

        if bl:

            add(
                "BILL_OF_LADING",
                "Shipper",
                val(mt700,"beneficiary"),
                val(bl,"shipper")
            )

            add(
                "BILL_OF_LADING",
                "Consignee",
                val(mt700,"applicant"),
                val(bl,"consignee")
            )

            add(
                "BILL_OF_LADING",
                "Goods",
                val(invoice,"goods"),
                val(bl,"goods_description")
            )

            add(
                "BILL_OF_LADING",
                "Gross Weight",
                val(packing,"gross_weight"),
                val(bl,"gross_weight")
            )

        # ===========================
        # CERTIFICATE OF ORIGIN
        # ===========================

        if co:

            add(
                "CERTIFICATE_OF_ORIGIN",
                "Exporter",
                val(mt700,"beneficiary"),
                val(co,"exporter")
            )

            add(
                "CERTIFICATE_OF_ORIGIN",
                "Importer",
                val(mt700,"applicant"),
                val(co,"consignee")
            )

            add(
                "CERTIFICATE_OF_ORIGIN",
                "Goods",
                val(invoice,"goods"),
                val(co,"goods_description")
            )

        # ===========================
        # INSURANCE
        # ===========================

        if insurance:

            add(
                "INSURANCE_CERTIFICATE",
                "Insured",
                val(mt700,"applicant"),
                val(insurance,"insured")
            )

            add(
                "INSURANCE_CERTIFICATE",
                "Beneficiary",
                val(mt700,"beneficiary"),
                val(insurance,"beneficiary")
            )

            add(
                "INSURANCE_CERTIFICATE",
                "Currency",
                val(mt700,"currency"),
                val(insurance,"currency")
            )

        

        # -------------------------------------------------
        # Latest Shipment Date
        # -------------------------------------------------

        try:

            if mt700 and bl:

                lc_date=getattr(mt700,"latest_shipment_date",None)
                bl_date=getattr(bl,"shipment_date",None)

                if lc_date and bl_date:

                    status="PASS"

                    if bl_date>lc_date:
                        status="FAIL"

                    rows.append({
                        "document":"BILL_OF_LADING",
                        "check":"Latest Shipment Date",
                        "status":status,
                        "expected":str(lc_date),
                        "actual":str(bl_date),
                    })

        except Exception:
            pass


        return rows
