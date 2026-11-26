# Reiwa year conversion

Use `to_reiwa` to convert a Gregorian year to a Japanese Reiwa era string.
The function takes a year as an integer and raises `ValueError` for years before 2019.

```python
from reiwa import to_reiwa

print(to_reiwa(2019))  # Reiwa 1
print(to_reiwa(2026))  # Reiwa 8
```

Install pytest with `python3 -m pip install pytest` if needed, then run the tests
from the repository root with `python3 -m pytest`.
