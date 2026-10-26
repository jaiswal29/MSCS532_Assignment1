"""Insertion sort in monotonically decreasing order.

MSCS 532 - Assignment 1
Author: Jatin Jaiswal

Based on INSERTION-SORT from Cormen, Leiserson, Rivest, and Stein,
*Introduction to Algorithms* (4th ed.), Section 2.1. The textbook procedure
sorts into monotonically increasing order. This implementation flips the
comparison in the inner while-loop so the array ends up in monotonically
decreasing order, i.e. A[0] >= A[1] >= ... >= A[n-1].

Textbook pseudocode (1-indexed) with the single change marked:

    INSERTION-SORT(A, n)
      for i = 2 to n
          key = A[i]
          // Insert A[i] into the sorted subarray A[1 : i-1].
          j = i - 1
          while j > 0 and A[j] > key        <-- here: A[j] < key
              A[j + 1] = A[j]
              j = j - 1
          A[j + 1] = key
"""


import argparse
import sys


def insertion_sort_decreasing(A, trace=False):
    """Sort the list A in place into monotonically decreasing order.

    Loop invariant (adapted from CLRS 4e, Section 2.1): at the start of
    each iteration of the for loop, the subarray A[0 : i] consists of the
    elements originally in A[0 : i], but in monotonically decreasing order.

    Args:
        A: a list of mutually comparable items (must support '<').
        trace: if True, print the array after each outer-loop iteration.

    Returns:
        The same list object, now sorted so that A[k] >= A[k+1] for all k.
    """
    n = len(A)
    # CLRS iterates i = 2..n over a 1-indexed array. In 0-indexed Python
    # that is i = 1..n-1; the single element A[0] is trivially sorted.
    for i in range(1, n):
        key = A[i]
        # Insert A[i] into the sorted subarray A[0 : i].
        j = i - 1
        # Shift every element that is SMALLER than key one slot to the
        # right. The textbook shifts elements GREATER than key; that one
        # comparison is the only difference between increasing and
        # decreasing order.
        while j >= 0 and A[j] < key:
            A[j + 1] = A[j]
            j -= 1
        A[j + 1] = key
        if trace:
            print(f"  i={i}: key={key!r:<4} -> {A}")
    return A


def _parse_number(token):
    """Parse a command-line token as int if possible, otherwise float."""
    try:
        return int(token)
    except ValueError:
        try:
            return float(token)
        except ValueError:
            raise argparse.ArgumentTypeError(f"not a number: {token!r}")


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Insertion sort into monotonically decreasing order "
                    "(CLRS 4e, Section 2.1 / Exercise 2.1-3)."
    )
    parser.add_argument(
        "numbers", nargs="*", type=_parse_number,
        help="numbers to sort; if omitted, the CLRS Figure 2.2 example is used",
    )
    parser.add_argument(
        "--trace", action="store_true",
        help="print the array after each outer-loop iteration",
    )
    args = parser.parse_args(argv)

    # Default: the example array from CLRS Figure 2.2.
    data = args.numbers if args.numbers else [5, 2, 4, 6, 1, 3]

    print("Input:              ", data)
    insertion_sort_decreasing(data, trace=args.trace)
    print("Sorted (decreasing):", data)
    return 0


if __name__ == "__main__":
    sys.exit(main())
