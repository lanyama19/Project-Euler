# Problem 21: Amicable numbers

## Problem Description

Let d(`n`) be defined as the sum of proper divisors of `n` (numbers less than `n` which divide evenly into `n`).

If d(`a`) = `b` and d(`b`) = `a`, where `a` ≠ `b`, then `a` and `b` are an amicable pair and each of `a` and `b` are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under `n`.

## Solution

The core idea is **"cache first, then search."** Calculating the sum of divisors independently for each number would involve a lot of redundant computation and be very inefficient. A much better approach is to pre-calculate and store the sum of proper divisors for all numbers under `n`, and then perform a single pass to find the numbers that meet the definition of an amicable pair.

***

### Step 1: Efficiently Calculate and Cache the Sum of Proper Divisors

The goal of this step is to create an array (or a hash map) that stores the sum of proper divisors, `d(i)`, for every number `i` from 1 to `n-1`. We can use a technique similar to a "sieve" to accomplish this quickly.

1. **Initialize an Array**: Create an array, let's call it `sums`, of size `n`, and initialize all its elements to `1`. We do this because `1` is a proper divisor of every number greater than `1`. `sums[i]` will be used to store the value of `d(i)`.
2. **Iterate and Accumulate Divisors**:
   * Start a loop with `i` from `2` up to `n/2`. Here, `i` represents a divisor.
   * For each `i`, loop through all multiples of `i` (i.e., `2*i`, `3*i`, `4*i`, ...) as long as the multiple `j` is less than `n`.
   * For each multiple `j`, add `i` to `sums[j]`.
   * After this process is complete, `sums[j]` will hold the total sum of `j`'s proper divisors.

**Example: Calculating `d(6)`**

* Initialization: `sums = [1, 1, 1, 1, 1, 1, 1, ...]`
* When `i = 2`, its multiples are `4, 6, 8, ...`. We add `2` to `sums[4]`, `sums[6]`, etc.
  * `sums[6]` becomes `1 + 2 = 3`.
* When `i = 3`, its multiples are `6, 9, 12, ...`. We add `3` to `sums[6]`, `sums[9]`, etc.
  * `sums[6]` becomes `3 + 3 = 6`.
* After the loops finish, we have `sums[6] = 6`, which is exactly the sum of the proper divisors of 6 (`1+2+3`).

By using this method, we can calculate the sum of proper divisors for all numbers with just one pass, which is much faster than prime factorization for each number. This is our **caching strategy**.

***

### Step 2: Iterate to Find and Sum Amicable Numbers

Now that we have the `sums` array containing the sum of proper divisors for all our numbers, finding the amicable ones is straightforward.

1. **Initialize Total Sum**: Create a variable `total_sum` and set it to `0`.
2. **Iterate and Check**:
   * Loop `a` from `2` up to `n-1`.
   * For each `a`, retrieve the pre-calculated sum of its proper divisors from our cache: `b = sums[a]`.
   * **Check the Amicable Conditions**:
     1. `a ≠ b` (By definition, the two numbers in an amicable pair must not be equal).
     2. `b < n` (This ensures that `b` is within the bounds of our array, so `sums[b]` is a valid lookup).
     3. `sums[b] == a` (This is the crucial reciprocal relationship: the sum of `b`'s proper divisors must equal `a`).
3. **Accumulate the Result**:
   * If the number `a` satisfies all three conditions above, it is an amicable number. Add it to `total_sum`.

This algorithm will naturally add both numbers of an amicable pair to the total. For example, when the loop reaches `a = 220`, it will find that `d(220) = 284` and `d(284) = 220`, so it will add `220` to the sum. Later, when the loop reaches `a = 284`, it will similarly find that `d(284) = 220` and `d(220) = 284`, and it will add `284` to the sum. No amicable numbers are missed or double-counted.

### Complexity Analysis

The efficiency of this algorithm can be analyzed in terms of time and space.

#### Time Complexity

1. **Calculating Divisor Sums (Step 1)**: The nested loops for pre-calculation dominate the runtime. The outer loop runs from `i = 2` to `n/2`. The inner loop runs for multiples of `i`. The total number of operations is approximately the sum of `n/i` for `i` from 2 to `n/2`, which is related to a harmonic series. This gives a time complexity of  $$O(n \log n)$$.
2. **Finding Amicable Pairs (Step 2)**: This involves a single loop from `2` to `n-1`. The operations inside the loop are array lookups, which are constant time $$O(1)$$. Therefore, this step has a time complexity of $$O(n)$$.

The overall time complexity is determined by the slower step, which is the pre-calculation. Thus, the total time complexity is $$O(n \log n)$$.

#### Space Complexity

The algorithm requires an array, `sums`, of size `n` to store the sum of proper divisors for each number up to `n`. Therefore, the space complexity is $$O(n)$$.

## Code

```python
def sum_amicable_numbers(n):
    """
    Evaluates the sum of all amicable numbers under n.
    """
    if n <= 1:
        return 0

    # Step 1: Efficiently calculate and cache the sum of proper divisors for all numbers.
    sums = [1] * n
    sums[0] = 0
    sums[1] = 0

    for i in range(2, n // 2 + 1):
        for j in range(2 * i, n, i):
            sums[j] += i

    # Step 2: Iterate to find and sum amicable numbers.
    total_sum = 0
    for a in range(2, n):
        b = sums[a]
        
        # Check the amicable conditions.
        if b < n and sums[b] == a and a != b:
            total_sum += a
            
    return total_sum

if __name__ == '__main__':
    test_cases = [1000, 2000, 5000, 10000]
    for limit in test_cases:
        result = sum_amicable_numbers(limit)
        print(f"The sum of all amicable numbers under {limit} is: {result}")
```

