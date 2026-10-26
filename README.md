# MSCS532_Assignment1 — Insertion Sort (Monotonically Decreasing Order)

**Course:** MSCS 532 — Algorithms and Data Structures, University of the Cumberlands
**Student:** Jatin Jaiswal
**Assignment 1:** Getting Started

## Goal

Implement the Insertion Sort algorithm from Chapter 2 of *Introduction to Algorithms*
(Cormen, Leiserson, Rivest, & Stein, 4th ed.), modified so that it sorts the input
array into **monotonically decreasing** order instead of increasing order
(this is Exercise 2.1-3 in the 4th edition).

## Files

| File | Purpose |
|---|---|
| `insertion_sort.py` | `insertion_sort_decreasing(A)` plus a small command-line demo |
| `test_insertion_sort.py` | 15 unit tests (`unittest`, standard library only) |

## Requirements

- Python 3.8 or higher. No third-party packages.

## How to run

```bash
# Sort the CLRS Figure 2.2 example array <5, 2, 4, 6, 1, 3>
python insertion_sort.py

# Sort your own numbers (ints or floats, negatives are fine)
python insertion_sort.py 31 41 59 26 41 58

# Show the array after every outer-loop iteration
python insertion_sort.py --trace

# Run the test suite
python -m unittest -v
```

Example output of `python insertion_sort.py --trace`:

```
Input:               [5, 2, 4, 6, 1, 3]
  i=1: key=2    -> [5, 2, 4, 6, 1, 3]
  i=2: key=4    -> [5, 4, 2, 6, 1, 3]
  i=3: key=6    -> [6, 5, 4, 2, 1, 3]
  i=4: key=1    -> [6, 5, 4, 2, 1, 3]
  i=5: key=3    -> [6, 5, 4, 3, 2, 1]
Sorted (decreasing): [6, 5, 4, 3, 2, 1]
```

The function can also be imported:

```python
from insertion_sort import insertion_sort_decreasing

A = [5, 2, 4, 6, 1, 3]
insertion_sort_decreasing(A)   # sorts in place and returns A
print(A)                       # [6, 5, 4, 3, 2, 1]
```

## The algorithm

CLRS (4th ed., Section 2.1) gives insertion sort for increasing order as:

```
INSERTION-SORT(A, n)
  for i = 2 to n
      key = A[i]
      // Insert A[i] into the sorted subarray A[1 : i-1].
      j = i - 1
      while j > 0 and A[j] > key
          A[j + 1] = A[j]
          j = j - 1
      A[j + 1] = key
```

The procedure keeps a sorted prefix `A[1 : i-1]` and, on each outer iteration, takes
the next element (`key`) and slides it leftward past every element that should come
*after* it, until it finds its slot. For increasing order the elements that must move
right are those **greater** than `key`.

To sort into decreasing order, exactly one thing changes: the elements that must move
right are those **smaller** than `key`. So the inner-loop condition `A[j] > key`
becomes `A[j] < key`. Everything else — the shifting, the index arithmetic, the final
placement — is unchanged. In 0-indexed Python this is:

```python
for i in range(1, n):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] < key:   # textbook: A[j] > key
        A[j + 1] = A[j]
        j -= 1
    A[j + 1] = key
```

Because the comparison is strict (`<`, not `<=`), elements equal to `key` are not
shifted, so equal keys keep their original relative order: the sort is **stable**,
exactly as the textbook version is.

## Why it is correct — the loop invariant

Following the structure CLRS uses in Section 2.1, the invariant for the outer loop is:

> At the start of each iteration of the `for` loop, the subarray `A[0 : i]`
> (elements `A[0]` through `A[i-1]`) consists of the elements originally in
> `A[0 : i]`, but in monotonically decreasing order.

- **Initialization.** Before the first iteration, `i = 1`, so the subarray is just
  `A[0]`. A single element is trivially in decreasing order, and it is the element
  that was originally there.
- **Maintenance.** The inner `while` loop moves `A[i-1], A[i-2], ...` one position to
  the right as long as each is *smaller* than `key`, then stops at the first position
  `j` where `A[j] >= key` (or at the front, `j = -1`). Placing `key` at `A[j+1]`
  therefore puts it immediately after everything that is `>= key` and immediately
  before everything that is `< key`. The subarray `A[0 : i+1]` is now the original
  elements of `A[0 : i+1]` in decreasing order, so the invariant holds for the next
  iteration (`i + 1`).
- **Termination.** The loop ends when `i = n`. Substituting into the invariant,
  `A[0 : n]` — the entire array — holds the original elements in monotonically
  decreasing order, which is what we wanted.

## Running time

Flipping the comparison does not change the cost structure; it only swaps which
inputs are the best and worst cases.

| Input | Inner-loop work | Total |
|---|---|---|
| Already **decreasing** (e.g. `[9, 7, 5, 3, 1]`) | 0 shifts per element | Θ(n) — best case |
| Already **increasing** (e.g. `[1, 3, 5, 7, 9]`) | `i` shifts for element `i` | Θ(n²) — worst case |
| Random order | about `i/2` shifts on average | Θ(n²) — average case |

It uses Θ(1) extra space because it sorts in place.

## Development process (commit history)

1. **Initial commit** — README describing the goal, `.gitignore`.
2. **Implement insertion sort in monotonically decreasing order** — transcribe the
   CLRS procedure to Python with the inner-loop comparison flipped; demo on the
   Figure 2.2 array.
3. **Add unit tests** — textbook examples, edge cases (empty, single, duplicates,
   negatives, floats, strings), best/worst-case inputs, in-place contract, stability,
   and 300 random lists checked against `sorted(reverse=True)`.
4. **Add CLI and complete the README** — accept numbers on the command line, add
   `--trace`, and document the loop invariant and running-time analysis.

## Reference

Cormen, T. H., Leiserson, C. E., Rivest, R. L., & Stein, C. (2022). *Introduction to
algorithms* (4th ed.). MIT Press.
