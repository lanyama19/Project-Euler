# Problem 14: Longest Collatz sequence

## Problem Description

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)

n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under the given `limit`, produces the longest chain?

**Note:** Once the chain starts the terms are allowed to go above `limit`.

## Solution

### Key Observations

* **Overlapping subproblems**: Many starting numbers eventually reach the same values (e.g., any chain hitting `16` will follow `16 → 8 → 4 → 2 → 1`).
* **Pure function**: The chain length for a given `n` always returns the same result and has no side effects — ideal for caching.
* **Values can exceed the limit**: The sequence may produce terms far greater than the starting value, so the cache must handle numbers well beyond the limit.

***

### Approach — Decorator-Based Caching

Use a caching decorator (such as `functools.lru_cache` with `maxsize=None`) on a function that computes the Collatz chain length for any integer `n`.

* **First call** for a given `n`: compute the length recursively and store it in the cache.
* **Subsequent calls** with the same `n`: return the stored result immediately in O(1) time.
* This ensures each unique integer’s chain length is computed only once, converting repeated recursion into simple cache lookups.

***

### Optimization Insight

For odd `n`, `3n + 1` is always even, so you can conceptually combine two steps:

1. Apply `n → 3n + 1`.
2. Immediately divide by 2.\
   This reduces the number of recursive calls and speeds up computation without changing the result.

***

### Algorithm Outline

1. **Base case:** The chain length for `n = 1` is 1.
2. **Recursive definition:**
   * Even `n`: length = 1 + length of `n / 2`.
   * Odd `n`: length = 2 + length of `(3n + 1) / 2` (using the combined step).
3. Iterate over all starting numbers from 2 up to `limit - 1`:
   * Compute the chain length using the cached function.
   * Track the maximum length and the starting number that produced it.
4. Return the starting number and its chain length.

***

### Complexity

Let `U` be the number of distinct integers encountered across all sequences up to the limit.

* **Time:** O(U), because each distinct value is computed exactly once.
* **Space:** O(U) for the cache (which may store numbers larger than the limit).

## Code

```python
from functools import lru_cache
from typing import Tuple

@lru_cache(maxsize=None)
def collatz_len(n: int) -> int:
    """
    Compute the length of the Collatz sequence starting from n (inclusive).
    - If n is even: next term is n / 2 (add 1 to length).
    - If n is odd:  next term is 3n + 1, which is always even, so we
      combine two steps into one: n -> 3n + 1 -> (3n + 1) / 2, and add 2 to length.
    Results are cached so each unique n is computed only once.
    """
    if n == 1:
        return 1
    if n % 2 == 0:
        # Even case: one step to n//2 plus the length from there
        return 1 + collatz_len(n // 2)
    # Odd case: fold two steps into one recursive call
    return 2 + collatz_len((3 * n + 1) // 2)

def longest_collatz_under(limit: int) -> Tuple[int, int]:
    """
    Find the starting number under `limit` that produces the longest Collatz chain.
    Returns a tuple: (starting_number, chain_length).
    """
    best_n, best_len = 1, 1
    # Test all starting numbers from 2 up to limit - 1
    for start in range(2, limit):
        length = collatz_len(start)
        # Update if this start has a longer chain
        if length > best_len:
            best_len, best_n = length, start
    return best_n, best_len

if __name__ == "__main__":
    # Run the function for given test limits and print results
    test_limits = [14, 5847, 46500, 54512, 100000, 1000000]
    for limit in test_limits:
        n, L = longest_collatz_under(limit)
        print(f"Limit: {limit} -> Start: {n}, Length: {L}")

```
