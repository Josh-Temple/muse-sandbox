import pytest

from reiwa import to_reiwa


@pytest.mark.parametrize(
    ("year", "expected"),
    [(2019, "Reiwa 1"), (2020, "Reiwa 2"), (2026, "Reiwa 8")],
)
def test_to_reiwa(year: int, expected: str) -> None:
    assert to_reiwa(year) == expected


def test_to_reiwa_rejects_year_before_2019() -> None:
    with pytest.raises(ValueError):
        to_reiwa(2018)
