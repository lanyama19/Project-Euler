# Problem 17: Number letter counts

## Problem Description

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to given `limit` inclusive were written out in words, how many letters would be used?

**Note:** Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

## Solution

Count letters by **decomposing each integer** and summing lengths of its parts:

* **1–19**: direct lookup (`one…nineteen`)
* **20–90**: tens words (`twenty, thirty, …, ninety`) + optional unit
* **100–999**: `<unit> + "hundred"` with **"and"** inserted **iff** there is a non-zero remainder (British usage)
* **1000**: `one thousand`

Ignore **spaces** and **hyphens**; only letters count. Use hash tables to store values mapping. Using a tiny **cache dictionary** avoids recomputing `1–99` many times.

## Code

```python
# Project Euler 17 — Number Letter Counts (British usage), small dict cache

# Base word lengths (letters only; no spaces/hyphens)
ONES_TEENS = {
    1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4,
    10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8
}
TENS = {20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6}  # "forty"=5
HUNDRED = 7   # "hundred"
THOUSAND = 8  # "thousand"
AND = 3       # "and"

_cache = {}   # small memo cache: n -> letter count

def letters_in_number(n: int) -> int:
    """Return the letter count for n written in British English words (1..1000)."""
    if n in _cache:
        return _cache[n]

    if n == 0:
        res = 0
    elif 1 <= n < 20:
        res = ONES_TEENS[n]
    elif 20 <= n < 100:
        tens = (n // 10) * 10
        rem = n % 10
        res = TENS[tens] + (ONES_TEENS[rem] if rem else 0)
    elif 100 <= n < 1000:
        hundreds = n // 100
        rem = n % 100
        res = ONES_TEENS[hundreds] + HUNDRED
        if rem:
            res += AND + letters_in_number(rem)
    elif n == 1000:
        res = ONES_TEENS[1] + THOUSAND  # "one thousand"
    else:
        raise ValueError("Supported range is 1..1000 inclusive.")

    _cache[n] = res
    return res

def total_letters(limit: int) -> int:
    """Sum letters for numbers 1..limit (British usage)."""
    if not (1 <= limit <= 1000):
        raise ValueError("limit must be between 1 and 1000 inclusive.")
    return sum(letters_in_number(i) for i in range(1, limit + 1))

if __name__ == "__main__":
    # Tests for 5, 15, 1000
    print("1..5   =", total_letters(5))     # expect 19
    print("1..15  =", total_letters(15))    # expect 74
    print("1..1000=", total_letters(1000))  # expect 21124

    # Optional assertions
    assert total_letters(5) == 19
    assert total_letters(15) == 74
    assert total_letters(1000) == 21124

```
