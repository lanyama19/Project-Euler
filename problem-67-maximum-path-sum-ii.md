# Problem 67: Maximum path sum II

## Problem Description

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

**3**\
**7** 4\
2 **4** 6\
8 5 **9** 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in `numTriangle`, a 2D array defined in the background containing a triangle with one-hundred rows.

**Note:** This is a much more difficult version of Problem 18. It is not possible to try every route to solve this problem, as there are 2<sup>99</sup> altogether! If you could check one trillion (10<sup>12</sup>) routes every second it would take over twenty billion years to check them all. There is an efficient algorithm to solve it. ;o)

The full data can be downloaded from Project Euler's website: [https://projecteuler.net/project/resources/p067\_triangle.txt](https://projecteuler.net/project/resources/p067_triangle.txt)

## Solution&#x20;

We can directly use the DP method from problem 18:

{% content-ref url="problem-18-maximum-path-sum-i.md" %}
[problem-18-maximum-path-sum-i.md](problem-18-maximum-path-sum-i.md)
{% endcontent-ref %}

## Code

```python
import urllib.request

def load_triangle_from_url(url: str) -> list[list[int]]:
    resp = urllib.request.urlopen(url)
    text = resp.read().decode('utf-8')
    triangle = [[int(num) for num in line.split()] for line in text.strip().split('\n')]
    return triangle

def max_path_sum(triangle: list[list[int]]) -> int:
    dp = triangle[-1][:]
    for r in range(len(triangle) - 2, -1, -1):
        for c in range(len(triangle[r])):
            dp[c] = triangle[r][c] + max(dp[c], dp[c + 1])
    return dp[0]

if __name__ == "__main__":
    url = "https://projecteuler.net/project/resources/p067_triangle.txt"
    try:
        tri = load_triangle_from_url(url)
        result = max_path_sum(tri)
        print("Problem 67 result:", result)
    except Exception as e:
        print("Error loading triangle from URL:", e)

```
