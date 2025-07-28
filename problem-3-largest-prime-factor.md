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

#### 3.1 Miller–Rabin

Given an odd $$n$$, write  $$n-1 = d,2^{s}$$ with $d$ odd. Choose a base $a$ coprime to $n$ and compute $x = a^{d} \bmod n$. If $x \not\in {1,n-1}$ and $x^{2^{r\}}\not\equiv n-1 \pmod n$ for all $0 \le r < s$, then $n$ is **composite**. Otherwise $n$ is _probably prime_. Using a handful of fixed bases makes the test _deterministic_ for 64‑bit integers.

#### 3.2 Pollard’s Rho Idea

Iterate a pseudorandom function

$$
x_{i+1} = x_i^2 + c \pmod n
$$

and look for a cycle. If $n = pq$ is composite, the sequences modulo $p$ and $q$ cycle at different speeds; their difference eventually reveals a non‑trivial factor via $\gcd\bigl(|x\_i - x\_j|,,n\bigr)$.

–– _“Rho” because the generated values trace a Greek‑letter ρ when drawn._ –

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
