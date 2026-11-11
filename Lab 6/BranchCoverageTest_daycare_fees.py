
import pytest
from daycare_fees import (
    extra_hours_fee,
    enrolment_allowed,
    pickup_status
)


# ==========================================
# EXTRA HOURS FEE - BRANCH COVERAGE
# ==========================================

@pytest.mark.parametrize("age_group,hours,sibling,expected", [
    # Included hours and extra hours
    ("infant", 20, False, 0),
    ("infant", 25, False, 70),

    # High extra hours - infant and non-infant
    ("infant", 45, False, 550),
    ("toddler", 50, False, 350),

    # Sibling conditions
    ("toddler", 35, True, 45),
    ("infant", 30, True, 140),
    ("preschool", 40, True, 45),

    # Different age groups
    ("preschool", 30, False, 0),
])
def test_extra_hours_branches(age_group, hours, sibling, expected):
    assert extra_hours_fee(age_group, hours, sibling) == expected


def test_invalid_age_group_branch():
    with pytest.raises(ValueError):
        extra_hours_fee("school", 20, False)


def test_negative_hours_branch():
    with pytest.raises(ValueError):
        extra_hours_fee("infant", -1, False)


# ==========================================
# ENROLMENT - BRANCH COVERAGE
# ==========================================

@pytest.mark.parametrize("age,vacancies,pending,expected", [
    # Immunisation pending - both outcomes
    (12, 0, True, True),
    (11, 0, True, False),

    # Immunisation not pending
    (24, 2, False, True),
    (24, 0, False, False),

    # Age below minimum
    (5, 2, False, False),

    # Boundary age
    (6, 1, False, True),
])
def test_enrolment_branches(age, vacancies, pending, expected):
    assert enrolment_allowed(age, vacancies, pending) is expected


# ==========================================
# PICKUP STATUS - BRANCH COVERAGE
# ==========================================

@pytest.mark.parametrize("minutes,aftercare,friday,expected", [
    # Regular pickup
    (10, False, False, "on_time"),
    (9, False, False, "late"),
    (-6, False, False, "overdue"),

    # Aftercare
    (20, True, False, "on_time"),
    (19, True, False, "late"),
    (4, True, False, "overdue"),

    # Friday
    (20, False, True, "on_time"),
    (19, False, True, "late"),
    (4, False, True, "overdue"),

    # Friday aftercare
    (30, True, True, "on_time"),
    (25, True, True, "late"),
    (14, True, True, "overdue"),
])
def test_pickup_branches(minutes, aftercare, friday, expected):
    assert pickup_status(minutes, aftercare, friday) == expected
