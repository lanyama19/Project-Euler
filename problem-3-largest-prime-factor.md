# Problem 3: Largest prime factor

## Promblem Description

The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the given `number`?

## Number Theory

### 1. Fundamental Theorem of Arithmetic

Every integer $$n > 1$$ can be written uniquely (up to the order of factors) as a product of primes:

$$
n \;=\; p_1^{\,\alpha_1}\,p_2^{\,\alpha_2}\,\dotsm p_k^{\,\alpha_k},
\qquad
p_1 < p_2 < \dots < p_k \text{ primes}.
$$

This guarantees that a “largest prime factor” is well defined—there is exactly one maximal $$p_k$$.

***

### 2. Square‑Root Bound for Trial Division

If $$n$$ is composite, it has **at least one** prime factor

$$
p \;\le\; \sqrt n .
$$

Proof: assume all factors were  $$> \sqrt n$$; the product of any two would exceed $$n$$, contradicting n’s factorisation.

> **Algorithmic consequence** To decide whether `n` is prime—or to strip off its smallest factor—it is enough to test divisibility by all primes up to $$\lfloor\sqrt n\rfloor$$

***

### 3. Probabilistic Primality Tests

### 3.1 Miller–Rabin

For an odd integer (n):

1. Write

$$
n - 1 =d \cdot2^{s}, \quad d \text{ is an odd}.
$$

Pick a base $$a$$ with $$\gcd(a,n)=1$$ and evaluate

$$
x = a^{d} \pmod{n}.
$$

**Decision rule**

* If $$x \in {1,,n-1}$$, the round “passes”.
* Otherwise square repeatedly: $$x \mapsto x^{2} \bmod n$$ for $$0 \le r < s$$\
  If none of these squarings yields `n-1`, then $$\displaystyle n$$ is **composite**.\
  If at least one does, the round passes and $$n$$ is **probably prime**.

Using the fixed bases $$\{2,3,5,7,11,13,17\}$$ makes the test **deterministic for every 64‑bit integer**.

### 3.2 Pollard’s Rho Idea

For a composite (n = pq) (distinct primes), define the pseudorandom map

$$
x_{i+1} = x_i^{,2} + c \pmod{n},\qquad c\neq 0
$$

* The sequences modulo `p` and modulo `q` enter cycles with generally different periods.
* Eventually two iterates satisfy $$x_i \equiv x_j \pmod{p}, \quad x_i \not\equiv x_j \pmod{q},$$ so the difference unveils a factor: $$g = \gcd\bigl(|x_i - x_j|, n\bigr) \in{p,q}.$$

Brent’s refinement detects the collision faster but the core principle is identical. “Rho” refers to the Greek letter ρ traced out by the states when plotted.

***

### Further Reading

| Title                                                         | Author(s)                         | Notes                                                                     |
| ------------------------------------------------------------- | --------------------------------- | ------------------------------------------------------------------------- |
| _An Introduction to the Theory of Numbers_ (6 th ed.)         | G. H. Hardy & E. M. Wright        | Classic reference for proofs of 1–3.                                      |
| _A Classical Introduction to Modern Number Theory_ (2 nd ed.) | Kenneth Ireland & Michael Rosen   | Chapters 3–4 cover unique factorisation and residue classes.              |
| _Prime Numbers: A Computational Perspective_ (2 nd ed.)       | Richard Crandall & Carl Pomerance | Excellent treatment of Miller–Rabin, Pollard’s Rho, and other algorithms. |
| _The Book of Prime Number Records_                            | Paulo Ribenboim                   | Historical context and deeper heuristics.                                 |
| _Implementing Number‑Theory Algorithms in C_                  | Richard S. Jaspan                 | Practical coding patterns (trial division, gcd, modular exponentiation).  |

> _These texts provide both the theoretical underpinnings and algorithmic details for efficient prime‑factor routines._ For hands‑on coding, Crandall & Pomerance is especially recommended.

## Code

```python
###############################################################################
# Version A — pure trial division (no MR, no Rho)
###############################################################################
def largest_prime_factor_vA(n: int) -> int:
    """Brute‑force: divide by every odd number up to sqrt(n)."""
    if n % 2 == 0:
        while n % 2 == 0:
            n //= 2
        if n == 1:
            return 2
    p, last = 3, 2
    while p * p <= n:
        if n % p == 0:
            last = p
            while n % p == 0:
                n //= p
        p += 2                      # every odd number
    return max(last, n)

###############################################################################
# Version B — 6k±1 trial + deterministic Miller–Rabin for 64‑bit inputs
###############################################################################
from math import gcd

_MR_BASES_64 = (2, 3, 5, 7, 11, 13, 17)

def _mod_pow(a, d, n):
    res = 1
    while d:
        if d & 1:
            res = (res * a) % n
        a = (a * a) % n
        d >>= 1
    return res

def is_prime_64(n: int) -> bool:
    """Deterministic Miller–Rabin for 0 < n < 2^64."""
    if n < 2:
        return False
    small = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
    if n in small:
        return True
    for p in small:
        if n % p == 0:
            return False
    # write n−1 = d·2^s
    d, s = n - 1, 0
    while d & 1 == 0:
        d >>= 1;  s += 1
    for a in _MR_BASES_64:
        x = _mod_pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False
    return True

def largest_prime_factor_vB(n: int) -> int:
    """6k±1 trial division; use MR to shortcut when remainder is prime."""
    if n % 2 == 0:
        last = 2
        while n % 2 == 0:
            n //= 2
    else:
        last = 1
    p = 3
    while p * p <= n:
        if n % p == 0:
            last = p
            while n % p == 0:
                n //= p
            if is_prime_64(n):
                return max(last, n)
        p += 2
        if p % 3 == 0:          # skip 6k+3
            p += 2
    return max(last, n)

###############################################################################
# Version C — Pollard’s Rho + Miller–Rabin  (Brent variant)
###############################################################################
import random

def _rho_brent(n: int) -> int:
    if n % 2 == 0:
        return 2
    y, c, m = random.randrange(1, n), random.randrange(1, n), 128
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for _ in range(r):
            y = (y * y + c) % n
        k = 0
        while k < r and g == 1:
            ys = y
            for _ in range(min(m, r - k)):
                y = (y * y + c) % n
                q = (q * abs(x - y)) % n
            g = gcd(q, n)
            k += m
        r <<= 1
    if g == n:
        while True:
            ys = (ys * ys + c) % n
            g = gcd(abs(x - ys), n)
            if 1 < g < n:
                break
    return g

def _factor(n: int, out: list):
    if n == 1:
        return
    if is_prime_64(n):
        out.append(n)
        return
    d = _rho_brent(n)
    _factor(d, out)
    _factor(n // d, out)

def largest_prime_factor_vC(n: int) -> int:
    """Full Pollard’s Rho recursion."""
    factors = []
    _factor(n, factors)
    return max(factors)

###############################################################################
# Quick smoke‑test
###############################################################################
if __name__ == "__main__":
    N = 600_851_475_143        # Project Euler #3 canonical value
    print("vA:", largest_prime_factor_vA(N))   # slowest
    print("vB:", largest_prime_factor_vB(N))   # faster
    print("vC:", largest_prime_factor_vC(N))   # fastest
```
