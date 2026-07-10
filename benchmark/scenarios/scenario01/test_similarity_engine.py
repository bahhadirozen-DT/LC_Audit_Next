from core.similarity.text_similarity import similarity


def test_equal():
    assert similarity("TEXTILE FABRICS","TEXTILE FABRICS")==100.0


def test_case():
    assert similarity("textile fabrics","TEXTILE FABRICS")==100.0


def test_partial():
    assert similarity(
        "TEXTILE FABRICS",
        "TEXTILE FABRICS POLYESTER"
    ) > 70


def test_different():
    assert similarity(
        "STEEL PIPE",
        "BANANA"
    ) < 30
