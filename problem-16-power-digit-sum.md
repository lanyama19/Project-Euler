# Problem 16: Power digit sum

## Problem Description

2<sup>15</sup> = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2<sup>`exponent`</sup>?

## Solution

Let $$N:=2^n$$. For each $$k\ge 1$$, define the residue&#x20;

$$
r_k := N \bmod 10^k
$$

i.e., the unique integer $$0\le r_k<10^k$$ with $$r_k\equiv N\pmod{10^k}$$.&#x20;

If $$N=\sum_{i=0}^{d-1} d_i10^i$$ is the decimal expansion (digits $$d_i\in{0,\dots,9}$$), then $$r_k=\sum_{i=0}^{k-1} d_i10^i.$$&#x20;

Hence $$d_{k-1}=\frac{r_k-r_{k-1}}{10^{k-1}},\  r_0:=0,$$ and the digit sum is $$\sum_i d_i$$.

***

### Definitions and Lemma (for completeness)

* **Decimal expansion.** $$N=\sum_{i=0}^{d-1} d_i,10^i$$, $$d=\lfloor n\log_{10}2\rfloor+1$$.
* **Residues.** $$r_k := N \bmod 10^k$$ (unique in $$[0,10^k-1]$$).

***

### Pseudo-code (No Big-Integer Construction)

```
FUNCTION DigitSumPowerOfTwo(n):
    # Number of decimal digits of 2^n
    d ← FLOOR(n * LOG10(2)) + 1

    sum ← 0
    r_prev ← 0        # r_0
    M ← 1             # current modulus = 10^(k-1)

    FOR k FROM 1 TO d:
        M ← M * 10                        # M = 10^k
        r ← ModExp(2, n, M)               # r_k = 2^n mod 10^k
        digit ← (r - r_prev) / (M / 10)   # d_{k-1}
        sum ← sum + digit
        r_prev ← r

    RETURN sum


FUNCTION ModExp(base, exp, mod):          # fast modular exponentiation
    result ← 1 % mod
    b ← base % mod
    e ← exp
    WHILE e > 0:
        IF (e MOD 2) = 1:
            result ← (result * b) MOD mod
        b ← (b * b) MOD mod
        e ← FLOOR(e / 2)
    RETURN result
```

**Loop invariant.** At each iteration (k), `r_prev = 2^n mod 10^(k-1)`. Thus `r - r_prev = d_{k-1}·10^{k-1}` is divisible by (10^{k-1}), so `digit ∈ {0,…,9}`.

***

### Complexity

* Outer loop runs $$d=\lfloor n\log_{10}2\rfloor+1$$ times.
* Each `ModExp` is $$O(\log n)$$.
* Total: $$O(d\log n)$$ time and $$O(1)$$ extra space (besides the growing modulus).

## Code

```python
import math

def digit_sum_power_of_two(n: int) -> int:
    """
    Compute the sum of decimal digits of 2^n
    without constructing 2^n itself.
    Space: O(1) extra.
    """

    # Number of decimal digits of 2^n
    d = int(math.floor(n * math.log10(2))) + 1 if n > 0 else 1

    total = 0
    r_prev = 0      # r_0
    M = 1           # current modulus = 10^(k-1)

    for _ in range(1, d + 1):
        M *= 10                        # M = 10^k
        r = pow(2, n, M)               # r_k = 2^n mod 10^k (fast modular power)
        digit = (r - r_prev) // (M // 10)  # d_{k-1} = (r_k - r_{k-1}) / 10^{k-1}
        total += digit
        r_prev = r

    # Quick sanity check (digit sum is congruent to 2^n mod 9)
    assert total % 9 == pow(2, n, 9), "Sanity check (mod 9) failed"
    return total


if __name__ == "__main__":
    tests = [15, 128, 1000]
    for exp in tests:
        s = digit_sum_power_of_two(exp)
        print(f"n = {exp:>4} → digit sum of 2^{exp} = {s}")

```
