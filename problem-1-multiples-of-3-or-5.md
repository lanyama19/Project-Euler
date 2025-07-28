# Problem1:  Multiples of 3 or 5

## Promblem Description

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below the provided parameter value `number`

## Solution Strategy

### 1. Recall the Arithmetic Series Formula

The sum of the first `n` terms of an arithmetic sequence with first term `a` and common difference `d` is:

$$
S_n = \frac{n}{2} \cdot (2a + (n - 1)d) ]
$$

However, for sequences starting with `a = d` (like 3, 6, 9, ...), this simplifies to the **triangular number formula**:

$$
S = d \cdot \frac{m(m + 1)}{2}
$$

Where:

* `d` is the base (e.g., 3 or 5),
* &#x20;`m`  is the number of terms under ( N ):&#x20;

***

### 2. Handle Double-Counting with Inclusion–Exclusion

If we sum all multiples of 3 and all multiples of 5 below ( N ), we will **double-count** numbers divisible by both 3 and 5 — i.e., multiples of 15.

To fix this, we apply the **inclusion–exclusion principle**

$$
\text{Sum} = \text{Sum}{3} + \text{Sum}{5} - \text{Sum}_{15}
$$

This ensures each multiple is counted only once.

## Code

```python
def sum_3_or_5_below(N: int) -> int:
    """
    Return the sum of all natural numbers below N that are divisible by 3 or 5.
    Uses the arithmetic progression formula for efficiency.
    """
    def sum_divisible_by(d: int) -> int:
        m = (N - 1) // d
        return d * m * (m + 1) // 2

    return (
        sum_divisible_by(3)
        + sum_divisible_by(5)
        - sum_divisible_by(15)  # subtract common multiples to fix double-counting
    )


if __name__ == "__main__":
    test_inputs = [10, 49, 1000, 8456, 19564]
    for n in test_inputs:
        result = sum_3_or_5_below(n)
        print(f"Sum of multiples of 3 or 5 below {n}: {result}")
```
