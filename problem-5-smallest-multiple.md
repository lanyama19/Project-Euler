# Problem 5: Smallest multiple

## Problem Description

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to `n`?

## Solution Strategy

We are looking for a number divisible by 1, 2, 3, ..., _n_. That is exactly the **Least Common Multiple.**

Instead of computing LCM step by step, we use **prime factorization**.

Every number between 1 and _n_ can be written as a product of primes. To make sure our result is divisible by all of them, we need to include:

* **Every prime ≤&#x20;**_**n**_
* With **the highest exponent** that still keeps the power ≤ _n_

That gives the formula:

$$
\text{LCM}(1..n) = \prod_{\text{prime } p \le n} p^{;\lfloor\log_p n\rfloor}
$$

Example (n = 10)

| Prime p | Max power ≤ 10 | p^k |
| ------- | -------------- | --- |
| 2       | 2³ = 8         | 8   |
| 3       | 3² = 9         | 9   |
| 5       | 5¹ = 5         | 5   |
| 7       | 7¹ = 7         | 7   |

Multiply: $$2^3 × 3^2 × 5 × 7 = 2520$$

***

## Code

<pre class="language-python"><code class="lang-python">import math
def smallest_multiple(n):
<strong>    is_prime = [True] * (n + 1)
</strong>    is_prime[0:2] = [False, False]
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n + 1, i):
                is_prime[j] = False
    primes = [i for i, ok in enumerate(is_prime) if ok]

    # Multiply max powers of all primes ≤ n
    result = 1
    for p in primes:
        k = int(math.log(n, p))
        result *= p**k
    return result


if __name__ == "__main__":
    # Test inputs
    test_inputs = [5, 7, 10, 13, 20]
    for n in test_inputs:
        print(f"LCM(1..{n}) = {smallest_multiple(n)}")
</code></pre>
