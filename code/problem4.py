def largest_palindrome_product(n: int) -> int:
    """Find the largest palindrome from product of two n-digit numbers."""
    hi = 10 ** n - 1
    lo = 10 ** (n - 1)

    for left in range(hi, lo - 1, -1):
        # Build even-length palindrome by mirroring 'left'
        p_str = str(left) + str(left)[::-1]
        p = int(p_str)

        # Start 'a' at the largest <= hi multiple of 11
        if hi % 11 == 0:
            a_start = hi
        else:
            a_start = hi - (hi % 11)
        # Loop over possible 'a', step -11
        for a in range(a_start, lo - 1, -11):
            if p % a == 0:
                b = p // a
                if lo <= b <= hi:
                    return p  # First found is the largest

    return None  # No palindrome found (should not happen for n >= 1)


if __name__ == "__main__":
    for n in range(2, 4):  # Try n=2,3,4 for demonstration
        ans = largest_palindrome_product(n)
        print(f"n = {n}: {ans}")