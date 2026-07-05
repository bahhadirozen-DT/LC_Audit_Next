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


        

        # =====================================================
        # REQUIRED DOCUMENTS (MT700 FIELD 46A)
        # =====================================================

        if mt700 and getattr(mt700, "required_documents", None):

            required = " ".join(mt700.required_documents).upper()

            checks = [
                ("COMMERCIAL INVOICE", invoice),
                ("PACKING LIST", packing),
                ("BILL OF LADING", bl),
                ("CERTIFICATE OF ORIGIN", co),
                ("INSURANCE", insurance),
            ]

            for name, obj in checks:

                expected = name in required
                uploaded = obj is not None

                if expected and not uploaded:
                    rows.append({
                        "check": f"Required Documents - {name}",
                        "document": "MT700",
                        "status": "FAIL",
                        "expected": "Required by LC",
                        "actual": "Missing",
                    })

                elif expected and uploaded:
                    rows.append({
                        "check": f"Required Documents - {name}",
                        "document": "MT700",
                        "status": "PASS",
                        "expected": "Required by LC",
                        "actual": "Uploaded",
                    })


        

        # =====================================================
        # INSURANCE POLICY vs CERTIFICATE
        # =====================================================

        if mt700 and insurance:

            specs = getattr(mt700, "required_document_specs", [])

            for s in specs:

                if s["document"] != "INSURANCE":
                    continue

                required_policy = s["policy"]

                insurance_type = str(
                    getattr(insurance, "document_name", "")
                ).upper()

                if required_policy and "CERTIFICATE" in insurance_type:

                    rows.append({
                        "check":"Insurance Policy Required",
                        "document":"INSURANCE_CERTIFICATE",
                        "status":"FAIL"
                    })


        

        # =====================================================
        # LEGALIZED CERTIFICATE OF ORIGIN
        # =====================================================

        if mt700 and co:

            specs = getattr(mt700, "required_document_specs", [])

            for s in specs:

                if s["document"] != "CERTIFICATE_OF_ORIGIN":
                    continue

                if not s["legalized"]:
                    continue

                legalized = bool(
                    getattr(co, "legalized", False)
                )

                if not legalized:

                    rows.append({
                        "check":"Legalized Certificate of Origin",
                        "document":"CERTIFICATE_OF_ORIGIN",
                        "status":"FAIL"
                    })


        

        # =====================================================
        # ORIGINAL / COPY COUNT
        # =====================================================

        doc_map = {
            "COMMERCIAL_INVOICE": invoice,
            "PACKING_LIST": packing,
            "BILL_OF_LADING": bl,
            "CERTIFICATE_OF_ORIGIN": co,
            "INSURANCE": insurance,
        }

        if mt700:

            specs = getattr(mt700, "required_document_specs", [])

            for spec in specs:

                obj = doc_map.get(spec["document"])

                if obj is None:
                    continue

                expected_originals = spec.get("originals", 0)
                expected_copies = spec.get("copies", 0)

                actual_originals = getattr(obj, "originals", None)
                actual_copies = getattr(obj, "copies", None)

                if expected_originals and actual_originals is not None:

                    if actual_originals != expected_originals:

                        rows.append({
                            "check":"Original Copy Count",
                            "document":spec["document"],
                            "status":"FAIL"
                        })

                if expected_copies and actual_copies is not None:

                    if actual_copies != expected_copies:

                        rows.append({
                            "check":"Copy Count",
                            "document":spec["document"],
                            "status":"FAIL"
                        })


        return rows
