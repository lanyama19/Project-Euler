# Problem 15: Lattice paths

## Problem Description

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

<p align="center"><img src=".gitbook/assets/image (2).png" alt=""></p>

How many such routes are there through a given `gridSize`?

## Solution

Any path from $$(0,0)$$ to $$(n,n)$$ contains exactly:

* $$n$$ moves **right** `R`
* $$n$$ moves **down** `D`

Total moves = 2n.\
The problem reduces to: _In a sequence of length 2n, choose which n positions are R._

The number of such sequences is the **central binomial coefficient**:

$$
\text{paths}(n) = \binom{2n}{n} = \frac{(2n)!}{(n!)^2}
$$

#### Example

For $$n=2$$, $$\binom{4}{2} = 6$$. These correspond exactly to the 6 unique paths in the diagram.

#### Efficient Computation

Instead of computing factorials directly, use the multiplicative formula:

$$
\binom{2n}{n} = \prod_{i=1}^n \frac{n+i}{i}
$$

&#x20;This keeps the intermediate results as integers and avoids huge factorials.

## Code

```python
import math

def lattice_paths(n: int) -> int:
    """Return the number of lattice paths through an n×n grid."""
    return math.comb(2 * n, n)

def lattice_paths_mul(n: int) -> int:
    """Compute C(2n, n) using multiplicative formula."""
    res = 1
    for i in range(1, n + 1):
        res = res * (n + i) // i
    return res

if __name__ == "__main__":
    for test_n in [4,9,20]:
        print(f"n={test_n}: {lattice_paths(test_n)} paths")
```
