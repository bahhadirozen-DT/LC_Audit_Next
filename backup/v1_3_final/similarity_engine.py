from core.similarity.company_matcher import match as company_match
from core.similarity.address_matcher import match as address_match
from core.similarity.hs_code_matcher import match as hs_match
from core.similarity.text_similarity import similarity
from core.similarity.goods_normalizer import normalize


class SimilarityEngine:

    def goods(self, a, b):

        return similarity(
            normalize(a),
            normalize(b),
        )

    def company(self, a, b):

        return company_match(a, b)

    def address(self, a, b):

        return address_match(a, b)

    def hs_code(self, a, b):

        return hs_match(a, b)
