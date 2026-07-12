class GoodsValidator:

    def validate(self, invoice, packing, bl):

        results = []

        goods = [
            getattr(invoice, "goods_description", None),
            getattr(packing, "goods_description", None),
            getattr(bl, "goods_description", None),
        ]

        goods = [g.strip() for g in goods if g]

        if len(set(goods)) > 1:
            results.append("GOODS_MISMATCH")
            results.append("GOODS_DESCRIPTION_MISMATCH")

        return results
