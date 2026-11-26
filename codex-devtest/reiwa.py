def to_reiwa(year: int) -> str:
    """Convert a Gregorian year to its Reiwa era string."""
    if year < 2019:
        raise ValueError("The Reiwa era starts in 2019.")
    return f"Reiwa {year - 2019 + 1}"
