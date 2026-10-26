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


def insertion_sort_decreasing(A):
    """Sort the list A in place into monotonically decreasing order.

    Returns the same list object so the call can be used as an expression.
    Elements must be mutually comparable with '<'.
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
    return A


if __name__ == "__main__":
    # The example array from CLRS Figure 2.2.
    data = [5, 2, 4, 6, 1, 3]
    print("Input:              ", data)
    insertion_sort_decreasing(data)
    print("Sorted (decreasing):", data)
