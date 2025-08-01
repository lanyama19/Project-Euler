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

