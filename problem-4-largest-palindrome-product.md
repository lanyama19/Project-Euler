# Problem 4: Largest palindrome product

### Problem Description

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two `n`-digit numbers.

### Solution Strategy

#### Key Observations

* `n`-digit numbers lie in the range `[lo, hi] = [10^(n-1), 10^n - 1]`.
* **Even-length palindromes are divisible by 11**, so at least one factor must be a multiple of 11.
* If palindromes are generated in descending order, the first one with valid `n`-digit factors is the maximum.

#### Algorithm (Palindrome-First + 11-Step Optimization)

1. Loop `left` from `hi` down to `lo`.
2. Build a palindrome `P = int(str(left) + str(left)[::-1])`.
3. For `a` from the largest ≤ `hi` multiple of 11 down to `ceil(P / hi)`, step `−11`:
   * If `P % a == 0`, set `b = P // a`.
   * If `lo ≤ b ≤ hi`, return `P`.

This works because:

* Palindromes are tested from largest to smallest.
* First match ensures the maximum result.

### Code

```python
def largest_palindrome_product(n: int) -> int:
    """Find the largest palindrome from product of two n-digit numbers."""
    hi = 10 ** n - 1
    lo = 10 ** (n - 1)

    for left in range(hi, lo - 1, -1):
        # Build even-length palindrome by mirroring 'left'
        p_str = str(left) + str(left)[::-1]
        p = int(p_str)

        # Start 'a' at the largest <= hi multiple of 11
        if hi % 11 == 0:
            a_start = hi
        else:
            a_start = hi - (hi % 11)
        # Loop over possible 'a', step -11
        for a in range(a_start, lo - 1, -11):
            if p % a == 0:
                b = p // a
                if lo <= b <= hi:
                    return p  # First found is the largest

    return None  # No palindrome found (should not happen for n >= 1)


if __name__ == "__main__":
    for n in range(2, 4):  # Try n=2,3,4 for demonstration
        ans = largest_palindrome_product(n)
        print(f"n = {n}: {ans}")
```
