# Problem 6: Sum square difference

## Problem Description

The sum of the squares of the first ten natural numbers is,

1<sup>2</sup> + 2<sup>2</sup> + ... + 10<sup>2</sup> = 385

The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)<sup>2</sup> = 55<sup>2</sup> = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640. Find the difference between the sum of the squares of the first `n` natural numbers and the square of the sum.

## Solution Strategy

Let

$$S = \displaystyle \sum_{k=1}^{n} k$$ , sum of the first n integers, $$Q = \displaystyle \sum_{k=1}^{n} k^{2}$$ be the sum of squares, $$D = S^{2} - Q$$ be the quantity we need.

We can prove that:

$$
S = \dfrac{n(n+1)}2 \\
Q = \dfrac{n(n+1)(2n+1)}6
$$

Plug into $$D = S^{2} - Q$$ we have

$$
\begin{aligned}
D(n) &= \Bigl[\tfrac{n(n+1)}2\Bigr]^{2}
       - \tfrac{n(n+1)(2n+1)}6 \\[4pt]
     &= \frac{n^{2}(n+1)^{2}}4
        -\frac{n(n+1)(2n+1)}6 \\[4pt]
     &= \frac{n(n+1)\bigl(3n^{2}-n-2\bigr)}{12} \\[4pt]
     &= \boxed{\displaystyle
        \frac{n(n-1)(n+1)(3n+2)}{12}}.
\end{aligned}
$$

## Code

```python
def sum_square_difference(n: int) -> int:
    """Return D(n) = (1+2+…+n)^2 − (1^2+2^2+…+n^2)."""
    return n * (n - 1) * (n + 1) * (3 * n + 2) // 12


if __name__ == "__main__":
    for n in [10, 20, 100]:
        print(f"n = {n:3d} → D(n) = {sum_square_difference(n)}")
```
