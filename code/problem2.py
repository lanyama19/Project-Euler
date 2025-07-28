def fiboEvenSum(n: int) -> int:
    """
    Return the sum of all even Fibonacci numbers less than or equal to n,
    using the recurrence relation E_k = 4*E_{k-1} + E_{k-2} for even terms.
    """
    prev, curr = 0, 2   # Initialize E_0 = 0, E_1 = 2
    total = 0

    while curr <= n:
        total += curr
        prev, curr = curr, 4 * curr + prev  # Compute next even Fibonacci number

    return total


# Test cases from the image
if __name__ == "__main__":
    test_cases = [
        (10, 10),
        (34, 44),
        (60, 44),
        (1000, 798),
        (100000, 60696),
        (4000000, 4613732),
    ]

    for i, (inp, expected) in enumerate(test_cases, 1):
        result = fiboEvenSum(inp)
        print(f"Test {i}: fiboEvenSum({inp}) = {result}  --> {'OK' if result == expected else 'FAIL'}")
