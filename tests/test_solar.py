from datetime import datetime

from src.calendar.solar import calculate_solar_datetime


def test_solar_datetime_returns_four_pillars():
    result = calculate_solar_datetime(datetime(1990, 5, 15, 10, 30))
    pillars = result["pillars"]
    assert set(pillars) == {"year", "month", "day", "hour"}
    assert all(len(value) == 2 for value in pillars.values())


def test_supported_year_range_is_enforced():
    try:
        calculate_solar_datetime(datetime(1800, 1, 1, 12, 0))
    except ValueError as exc:
        assert "1900-2100" in str(exc)
    else:
        raise AssertionError("expected unsupported year to raise ValueError")
