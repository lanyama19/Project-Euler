# Problem 10: Summation of primes

## Problem Description

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17. Find the sum of all the primes below `n`.

## Solution

We use the **Sieve of Eratosthenes** algorithm, which efficiently generates all primes less than n.

#### Steps

1. **Initialize**
   * Create a boolean array `is_prime[0‥n)` and set all entries to `True`, except for 0 and 1.
2. **Sieve Process**
   * For each integer `p` from 2 up to `√n`:
     * If `is_prime[p]` is `True`, mark all multiples of `p` (from `p*p` up to `n-1`) as `False`.
3. **Sum Primes**
   * The indices still marked `True` in `is_prime` are primes. Sum all such indices.

#### Time & Space Complexity

| Type  | Order          |
| ----- | -------------- |
| Time  | O(n log log n) |
| Space | O(n)           |

#### Why is the Sieve of Eratosthenes  $$O(n log log n)$$?

**Main Idea**

* For each prime $$p ≤ n$$, the sieve marks all multiples of p as not prime, starting from $$p²$$.
* The number of markings for each prime p is about $$n / p$$.

**Total Operations**

* The total number of times we mark a composite is:

$$
\sum_{p \leq n} \left\lfloor \frac{n}{p} \right\rfloor \approx n \sum_{p \leq n} \frac{1}{p}
$$

where the sum is over all primes $$p ≤ n$$.

* The sum of reciprocals of all primes up to n is well-known to be:

$$
\sum_{p \leq n} \frac{1}{p} \approx \log \log n
$$

**Final Complexity**

* Therefore, the total time is: $$O\left(n \log\log n\right)$$
* The log log n term grows very slowly, making the sieve very efficient for large `n`.

**Summary**

> The Sieve of Eratosthenes is so fast because it efficiently skips redundant checks, and the total work needed is proportional to n times the sum of reciprocals of all primes up to n, which grows like log log n

## Code Implementation

```python
def sum_of_primes(n):
    """
    Returns the sum of all prime numbers less than n using the Sieve of Eratosthenes.
    :param n: Upper bound (not inclusive)
    :return: Sum of all primes less than n
    """
    if n < 2:
        return 0  # No primes below 2

    # Step 1: Create a boolean array where index i represents if 'i' is prime
    is_prime = [True] * n
    is_prime[0] = False
    is_prime[1] = False

    # Step 2: Sieve process
    from math import isqrt
    for p in range(2, isqrt(n) + 1):
        if is_prime[p]:
            for multiple in range(p * p, n, p):
                is_prime[multiple] = False

    # Step 3: Sum all primes
    return sum(i for i, prime in enumerate(is_prime) if prime)


if __name__ == "__main__":
    # Test cases
    test_cases = [17, 2001, 140759, 2000000]
    for n in test_cases:
        result = sum_of_primes(n)
        print(f"Sum of primes less than {n}: {result}")
```
