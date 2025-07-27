---
title: "Project Euler Problem 1"
---

<style>
h1, h2, h3 { border-bottom: 1px solid #eaecef; padding-bottom: 0.3em; }
code { background-color: #f6f8fa; padding: 2px 4px; border-radius: 4px; }
pre code { background-color: #f6f8fa; display: block; padding: 10px; }
</style>

# 🧮 Project Euler Problem 1 – Multiples of 3 or 5

Calculate the sum of all natural numbers **below** a given limit `N` that are divisible by 3 **or** 5.

---

## 📐 Formula

Let:

- \( m_3  = \left\lfloor \frac{N - 1}{3} \right\rfloor \)
- \( m_5  = \left\lfloor \frac{N - 1}{5} \right\rfloor \)
- \( m_{15} = \left\lfloor \frac{N - 1}{15} \right\rfloor \)

Then:

```text
sum = 3  * m3  * (m3  + 1) / 2
    + 5  * m5  * (m5  + 1) / 2
    - 15 * m15 * (m15 + 1) / 2
```

This works because:

1. Multiples of 3 and 5 form arithmetic sequences.
2. Their sums can be calculated with the triangular number formula:

   \[
   S = d \cdot \frac{m(m+1)}{2}
   \]

3. Multiples of 15 are double-counted, so we subtract them once.

---

## 🐍 Python Implementation

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

**Example usage:**

```python
>>> sum_3_or_5_below(10)
23

>>> sum_3_or_5_below(1000)
233168
```

---

## ⏱ Complexity

- **Time:** \( O(1) \)
- **Memory:** \( O(1) \)

---

## 📜 License

MIT License – free to copy, modify, and share.
