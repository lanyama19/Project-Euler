    # Project Euler Problem&nbsp;1 – Multiples of 3 or 5

    Calculate the sum of all natural numbers **below** a given limit `N` that are divisible by 3 **or** 5.

    ---

    ## Formula

    Let

    * `m3  = ⌊(N − 1)/3⌋`  – count of multiples of 3 below `N`
    * `m5  = ⌊(N − 1)/5⌋`  – count of multiples of 5 below `N`
    * `m15 = ⌊(N − 1)/15⌋` – count of multiples of 15 below `N` (to fix double‑counting)

    The closed‑form sum is:

    ```text
    sum = 3  * m3  * (m3  + 1) / 2
        + 5  * m5  * (m5  + 1) / 2
        - 15 * m15 * (m15 + 1) / 2
    ```

    **Why it works**

    1.  All multiples of 3 form an arithmetic progression `3, 6, 9, …` with common difference 3.  
        The sum of the first `m3` terms is `3 * m3*(m3+1)/2`.
    2.  Ditto for multiples of 5.  
    3.  Multiples of 15 have been counted twice (once in each list), so subtract them once.  
       This is the inclusion–exclusion principle.

    Each series collapses to the triangular‑number formula


\[\displaystyle S = d \cdot \frac{m(m+1)}{2}\]

    because the first term equals the common difference.

    ---

    ## Tiny Python helper

    ```python
    def sum_3_or_5_below(N: int) -> int:
        """Return Σ{k < N, k mod 3 == 0 or k mod 5 == 0}."""
        m3  = (N - 1) // 3
        m5  = (N - 1) // 5
        m15 = (N - 1) // 15
        return (3  * m3  * (m3  + 1) // 2 +
                5  * m5  * (m5  + 1) // 2 -
                15 * m15 * (m15 + 1) // 2)
    ```

    **Usage example**

    ```python
    >>> sum_3_or_5_below(10)
    23
    >>> sum_3_or_5_below(1000)   # Project Euler official test
    233168
    ```

    ---

    ## Complexity

    * **Time:** `O(1)` – only a few integer operations  
    * **Memory:** `O(1)` – constant space

    ---

    ## License

    MIT License – free to copy, modify, and share.
