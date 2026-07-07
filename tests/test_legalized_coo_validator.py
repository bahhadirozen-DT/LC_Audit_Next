from core.validation.legalized_coo_validator import LegalizedCOOValidator


def test_fail():

    r = LegalizedCOOValidator().validate(
        True,
        False
    )

    assert r["status"] == "FAIL"


def test_pass_required():

    r = LegalizedCOOValidator().validate(
        True,
        True
    )

    assert r["status"] == "PASS"


def test_not_required():

    r = LegalizedCOOValidator().validate(
        False,
        False
    )

    assert r["status"] == "PASS"
