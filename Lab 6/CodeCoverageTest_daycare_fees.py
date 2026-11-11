
import pytest
from daycare_fees import (
    extra_hours_fee,
    enrolment_allowed,
    pickup_status
)


# ==========================================
# EXTRA HOURS FEE TESTS
# ==========================================

def test_within_included_hours():
    assert extra_hours_fee("toddler", 20, False) == 0


def test_invalid_age_group():
    with pytest.raises(ValueError, match="unknown age group"):
        extra_hours_fee("school", 30, False)


def test_negative_hours():
    with pytest.raises(ValueError, match="invalid hours"):
        extra_hours_fee("infant", -5, False)


def test_sibling_discount():
    assert extra_hours_fee("toddler", 30, True) == 0


def test_infant_extra_hours():
    assert extra_hours_fee("infant", 25, False) == 70


def test_infant_high_extra_hours():
    assert extra_hours_fee("infant", 45, False) == 550


def test_toddler_high_extra_hours():
    assert extra_hours_fee("toddler", 50, False) == 350


# ==========================================
# ENROLMENT TESTS
# ==========================================

def test_enrolment_allowed():
    assert enrolment_allowed(24, 2, False) is True


def test_pending_immunisation():
    assert enrolment_allowed(12, 0, True) is True


def test_age_below_minimum():
    assert enrolment_allowed(5, 2, False) is False


# ==========================================
# PICKUP STATUS TESTS
# ==========================================

def test_pickup_on_time():
    assert pickup_status(25, False, False) == "on_time"


def test_pickup_late():
    assert pickup_status(5, False, False) == "late"


def test_pickup_overdue():
    assert pickup_status(-6, False, False) == "overdue"


def test_friday_aftercare():
    assert pickup_status(30, True, True) == "on_time"
