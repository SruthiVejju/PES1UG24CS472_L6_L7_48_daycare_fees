import pytest
from hypothesis import given, strategies as st
from daycare_fees import parse_enrolment, hours_average, payable_fee


@given(st.text() | st.none())
def test_parse_enrolment_no_unexpected_crash(s):
    try:
        result = parse_enrolment(s)
        assert isinstance(result, tuple)
    except ValueError:
        pass
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")


@given(st.text() | st.none())
def test_hours_average_no_unexpected_crash(s):
    try:
        result = hours_average(s)
        assert isinstance(result, int)
    except ValueError:
        pass
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")


@given(st.text() | st.none())
def test_payable_fee_no_unexpected_crash(s):
    try:
        result = payable_fee(s)
        assert isinstance(result, (int, float))
    except ValueError:
        pass
    except Exception as e:
        pytest.fail(f"Unexpected error: {e}")