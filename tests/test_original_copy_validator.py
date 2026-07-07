from core.validation.original_copy_validator import OriginalCopyValidator


def test_original_fail():

    r = OriginalCopyValidator().validate(
        3, 2,
        1, 2
    )

    assert r["status"] == "FAIL"


def test_copy_fail():

    r = OriginalCopyValidator().validate(
        1, 3,
        1, 1
    )

    assert r["status"] == "FAIL"


def test_pass():

    r = OriginalCopyValidator().validate(
        2, 2,
        2, 3
    )

    assert r["status"] == "PASS"
