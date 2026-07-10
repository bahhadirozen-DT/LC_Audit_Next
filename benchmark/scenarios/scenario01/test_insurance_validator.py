from core.validation.insurance_validator import InsuranceValidator


def test_policy_fail():

    r = InsuranceValidator().validate(
        True,
        False,
        False,
        True,
    )

    assert r["status"] == "FAIL"


def test_certificate_fail():

    r = InsuranceValidator().validate(
        False,
        True,
        True,
        False,
    )

    assert r["status"] == "FAIL"


def test_pass():

    r = InsuranceValidator().validate(
        True,
        False,
        True,
        False,
    )

    assert r["status"] == "PASS"
