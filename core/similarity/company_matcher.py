from core.similarity.text_similarity import similarity


def match(a, b):

    score = similarity(a, b)

    return {
        "score": score,
        "matched": score >= 92,
    }
