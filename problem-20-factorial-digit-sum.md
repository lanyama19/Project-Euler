# Problem 20: Factorial digit sum

## Problem Description

`n`! means `n` × (`n` − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,\
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits `n`!

## Solution

The solution is to simulate the process of long multiplication by hand. Instead of representing the factorial as a single large integer, we represent it as an **array or list of its digits**. The calculation proceeds iteratively, multiplying this list of digits by `2, 3, 4, ..., n`, and updating the digits and any carry-over at each step.

### Algorithm Steps

1. **Representation**: We use a list of integers to store the number, with the least significant digit at the beginning of the list (index 0). For example, the number `591` would be stored as `[1, 9, 5]`.
2. **Initialization**: Start with a list `digits = [1]`, which represents the initial value of `1!`.
3. **Iterative Multiplication**: Loop a multiplier `i` from `2` up to `n`. In each iteration, multiply the number represented by `digits` by `i`.
4. **Digit-by-Digit Multiplication**: To multiply the `digits` list by `i`, perform the following:
   * Initialize a `carry` variable to `0`.
   * Create a new empty list to store the result.
   * For each digit `d` in the `digits` list:
     * Calculate `product = d * i + carry`.
     * The new digit for the result is `product % 10`.
     * The new `carry` is `product // 10`.
   * After iterating through all digits, append any remaining `carry` to the result list.
   * Replace the old `digits` list with the newly computed one.
5. **Final Summation**: After the loop from `2` to `n` completes, the `digits` list holds the individual digits of $$n!$$. The final answer is the sum of all elements in this list.

## Code

```python
def factorial_digit_sum(n: int) -> int:
    """
    Calculates the sum of the digits of n! using a digit array method.
    """
    if n < 0:
        return 0
    
    digits = [1]
    
    for i in range(2, n + 1):
        carry = 0
        for j in range(len(digits)):
            product = digits[j] * i + carry
            digits[j] = product % 10
            carry = product // 10
        
        while carry > 0:
            digits.append(carry % 10)
            carry //= 10
            
    return sum(digits)

if __name__ == "__main__":
    test_cases = [10, 25, 50, 75, 100]
    
    print("Calculating the sum of digits for n!:")
    for n_val in test_cases:
        result = factorial_digit_sum(n_val)
        print(f"n = {n_val:<3} -> Sum = {result}")
```
