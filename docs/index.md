# Project Euler Problem 1 – Multiples of 3 or 5

Calculate the sum of all natural numbers **below** a given limit `N` that are divisible by 3 **or** 5.

## Formula

Let:
- m₃ = ⌊(N - 1) / 3⌋
- m₅ = ⌊(N - 1) / 5⌋
- m₁₅ = ⌊(N - 1) / 15⌋

Then:
```
sum = 3  * m3  * (m3  + 1) / 2
    + 5  * m5  * (m5  + 1) / 2
    - 15 * m15 * (m15 + 1) / 2
```

This works because:
1. Multiples of 3 and 5 form arithmetic sequences.
2. Their sums can be calculated with the triangular number formula: S = d × m(m+1)/2
3. Multiples of 15 are double-counted, so we subtract them once.

## Python Implementation

```python
def sum_3_or_5_below(N: int) -> int:
    """Return sum of numbers below N divisible by 3 or 5."""
    m3  = (N - 1) // 3
    m5  = (N - 1) // 5
    m15 = (N - 1) // 15
    return (3  * m3  * (m3  + 1) // 2 +
            5  * m5  * (m5  + 1) // 2 -
            15 * m15 * (m15 + 1) // 2)
```

**Example usage:**
```python
>>> sum_3_or_5_below(10)
23
>>> sum_3_or_5_below(1000)
233168
```

## Complexity

- **Time:** O(1)
- **Memory:** O(1)

## License

MIT License – free to copy, modify, and share.