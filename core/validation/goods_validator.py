class GoodsValidator:
    def validate(self, invoice, packing, bl):
        goods = {
            getattr(invoice, "goods_description", None),
            getattr(packing, "goods_description", None),
            getattr(bl, "goods_description", None),
        }
        goods.discard(None)
        return [] if len(goods) <= 1 else ["GOODS_MISMATCH"]
