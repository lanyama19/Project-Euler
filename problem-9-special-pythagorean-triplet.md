# Problem 9: Special Pythagorean triplet

## Problem Description

A Pythagorean triplet is a set of three natural numbers, `a` < `b` < `c`, for which,

a<sup>2</sup> + b<sup>2</sup> = c<sup>2</sup>

For example, 3<sup>2</sup> + 4<sup>2</sup> = 9 + 16 = 25 = 5<sup>2</sup>.

There exists exactly one Pythagorean triplet for which `a` + `b` + `c` = 1000. Find the product `abc` such that `a` + `b` + `c` = `n`.

## Solution

### 1. Euclid’s Formula for Pythagorean Triplets

Any Pythagorean triplet (primitive or scaled) can be written as:

$$
\begin{aligned} a_0 &= m^2 - n^2, \ b_0 = 2mn , c_0 = m^2 + n^2 \end{aligned}
$$

Where:

* $$m > n \geq 1$$
* $$m, n$$ are coprime and have opposite parity (one even, one odd)

Every scaled triplet is formed by multiplying the primitive triplet by an integer $$( k \geq 1 )$$:

$$a = k \cdot a_0, \  b = k \cdot b_0, \  c = k \cdot c_0$$

The perimeter is:

$$
a + b + c = k \cdot (a_0 + b_0 + c_0) = k \cdot [2m(m+n)]
$$

***

### 2. Reducing to a Search Problem

Given perimeter $$P = 2km(m+n)$$:

Let $$p = P / 2$$ so:

$$
p = km(m+n)
$$

We seek integers $$(k, m, n)$$ satisfying this equation and the parameter conditions above.

***

### 3. Search Strategy

* Loop $$m$$ from 2 to $$\sqrt{p}$$:\
  If $$m$$ does not divide $$p$$, continue.
* Let $$q = p / m$$:\
  For all $$d > m$$ such that $$d \mid q$$:
* Set $$n = d - m,  \ k = q / d$$:\
  Check: $$n > 0$$, $$\gcd(m, n) = 1$$, and $$m$$ and $$n$$ have opposite parity.
* Compute triplet using Euclid’s formula:\
  If  $$a < b < c$$  and $$a + b + c = P$$, output `abc`.

***

### 4. Complexity

* **Time:** $$O(\sqrt{P})$$, much faster than brute-force `(a,b)` search.
* **Space:** $$O(1)$$

## Python Code Implementation

```python
from math import gcd

def all_special_triplets(P):
    """
    Returns a list of tuples (a, b, c, product) for all Pythagorean triplets
    such that a < b < c, a + b + c = P, and a^2 + b^2 = c^2.
    Only positive integer solutions are returned.
    """
    triplets = []
    p = P // 2
    for m in range(2, int(p ** 0.5) + 1):
        if p % m != 0:
            continue
        q = p // m
        for d in range(m + 1, q + 1):
            if q % d != 0:
                continue
            n = d - m
            k = q // d
            if n <= 0 or (m - n) % 2 == 0 or gcd(m, n) != 1:
                continue
            a = k * (m * m - n * n)
            b = k * (2 * m * n)
            c = k * (m * m + n * n)
            # All sides must be positive and a < b < c
            sides = sorted([a, b, c])
            if all(x > 0 for x in sides) and sides[0] < sides[1] < sides[2] and sum(sides) == P:
                triplet = (sides[0], sides[1], sides[2], sides[0] * sides[1] * sides[2])
                if triplet not in triplets:  # Avoid duplicates
                    triplets.append(triplet)
    return triplets

if __name__ == "__main__":
    test_input = [24, 120, 1000]
    for P in test_input:
        print(f"P = {P}:")
        solutions = all_special_triplets(P)
        if solutions:
            for idx, (a, b, c, product) in enumerate(solutions, 1):
                print(f"  Solution {idx}: a={a}, b={b}, c={c}, abc={product}")
        else:
            print("  No solution found.")
        print()
```
