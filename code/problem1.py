def sum_3_or_5_below(N: int) -> int:
    """
    Return the sum of all natural numbers below N that are divisible by 3 or 5.
    Uses the arithmetic progression formula for efficiency.
    """
    def sum_divisible_by(d: int) -> int:
        m = (N - 1) // d
        return d * m * (m + 1) // 2

    return (
        sum_divisible_by(3)
        + sum_divisible_by(5)
        - sum_divisible_by(15)  # subtract common multiples to fix double-counting
    )


if __name__ == "__main__":
    test_inputs = [10, 49, 1000, 8456, 19564]
    for n in test_inputs:
        result = sum_3_or_5_below(n)
        print(f"Sum of multiples of 3 or 5 below {n}: {result}")