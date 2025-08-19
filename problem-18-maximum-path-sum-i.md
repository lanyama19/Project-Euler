# Problem 18: Maximum path sum I

## Problem Description

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

**3**\
**7** 4\
2 **4** 6\
8 5 **9** 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75\
95 64\
17 47 82\
18 35 87 10\
20 04 82 47 65\
19 01 23 75 03 34\
88 02 77 73 07 63 67\
99 65 04 28 06 16 70 92\
41 41 26 56 83 40 80 70 33\
41 48 72 33 47 32 37 16 94 29\
53 71 44 65 25 43 91 52 97 51 14\
70 11 33 28 77 73 17 78 39 68 17 57\
91 71 52 38 17 14 91 43 58 50 27 29 48\
63 66 04 68 89 53 67 30 73 16 69 87 40 31\
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

**NOTE:** As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)

## Solution

### Key Insight

A naive brute force approach would try all possible paths, which grows exponentially with the number of rows. However, this problem exhibits **optimal substructure**, which makes it a good candidate for **dynamic programming (DP)**.

***

### DP State Definition

Let $$S(r, c) = \text{the maximum path sum from position } (r, c) \text{ down to the bottom}$$

* Here, `r` is the row index (0-based from the top).
* `c` is the column index in that row.

***

### Recurrence Relation

From position `(r, c)`, the next step must go to either:

* Left child `(r+1, c)`
* Right child `(r+1, c+1)`

Therefore, the best path sum from `(r, c)` is: $$S(r, c) = a(r, c) + \max\big(S(r+1, c), S(r+1, c+1)\big)$$

where `a(r,c)` is the value at that position.

***

### Base Case

At the bottom row (say row `R-1`), there are no further steps: $$S(R-1, c) = a(R-1, c)$$

***

### Algorithm (Bottom-Up Approach)

1. Initialize `dp` as the values of the last row.
2. Iterate upward from the second-to-last row to the top:
   * For each position `(r, c)`, update: $$dp[c] \leftarrow a(r,c) + \max(dp[c], dp[c+1])$$
   * This collapses the bottom row into the row above, progressively reducing the triangle.
3. After processing all rows, the answer is stored in `dp[0]`.

***

### Complexity Analysis

* **Time Complexity:**\
  Each element is processed exactly once, and each update requires constant time.\
  Total complexity:\
  $$O(n^2) \quad \text{for a triangle with } n \text{ rows}$$
* **Space Complexity:**\
  We only need one array `dp` to store results of the current row, of length `n`.\
  Space complexity: $$O(n)$$

## Code

```python
def max_path_sum(triangle):
    """
    Compute the maximum path sum from top to bottom of a triangle.
    """
    # start from the bottom row
    dp = triangle[-1][:]
    # iterate upward
    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r])):
            dp[c] = triangle[r][c] + max(dp[c], dp[c + 1])
    return dp[0]


if __name__ == "__main__":
    # small test case
    small_triangle = [
        [3],
        [7, 4],
        [2, 4, 6],
        [8, 5, 9, 3],
    ]
    print("Small triangle result:", max_path_sum(small_triangle))  # Expected 23

    # main problem triangle
    triangle = [
        [75],
        [95, 64],
        [17, 47, 82],
        [18, 35, 87, 10],
        [20,  4, 82, 47, 65],
        [19,  1, 23, 75,  3, 34],
        [88,  2, 77, 73,  7, 63, 67],
        [99, 65,  4, 28,  6, 16, 70, 92],
        [41, 41, 26, 56, 83, 40, 80, 70, 33],
        [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
        [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
        [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
        [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
        [63, 66,  4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
        [ 4, 62, 98, 27, 23,  9, 70, 98, 73, 93, 38, 53, 60,  4, 23],
    ]

    print("Main triangle result:", max_path_sum(triangle))
```
