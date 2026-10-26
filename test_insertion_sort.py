"""Unit tests for insertion_sort_decreasing.

Run with:  python -m unittest -v
"""

import random
import unittest

from insertion_sort import insertion_sort_decreasing


class _Keyed:
    """Item that compares only on `key`, used to check stability."""

    def __init__(self, key, tag):
        self.key = key
        self.tag = tag

    def __lt__(self, other):
        return self.key < other.key

    def __repr__(self):
        return f"{self.key}{self.tag}"


class TestInsertionSortDecreasing(unittest.TestCase):

    def assert_monotonically_decreasing(self, A):
        for k in range(len(A) - 1):
            self.assertGreaterEqual(A[k], A[k + 1], msg=f"not decreasing at index {k}: {A}")

    # --- basic behaviour -------------------------------------------------

    def test_textbook_example(self):
        # Figure 2.2 input, expected in decreasing order
        self.assertEqual(insertion_sort_decreasing([5, 2, 4, 6, 1, 3]), [6, 5, 4, 3, 2, 1])

    def test_exercise_2_1_1_input(self):
        self.assertEqual(
            insertion_sort_decreasing([31, 41, 59, 26, 41, 58]),
            [59, 58, 41, 41, 31, 26],
        )

    def test_empty_list(self):
        self.assertEqual(insertion_sort_decreasing([]), [])

    def test_single_element(self):
        self.assertEqual(insertion_sort_decreasing([7]), [7])

    def test_two_elements(self):
        self.assertEqual(insertion_sort_decreasing([1, 2]), [2, 1])
        self.assertEqual(insertion_sort_decreasing([2, 1]), [2, 1])

    # --- special shapes --------------------------------------------------

    def test_already_decreasing_is_unchanged(self):
        # Best case for insertion sort: inner loop never runs
        A = [9, 7, 5, 3, 1]
        self.assertEqual(insertion_sort_decreasing(list(A)), A)

    def test_increasing_input_is_reversed(self):
        # Worst case: every element shifts all the way to the front
        self.assertEqual(insertion_sort_decreasing(list(range(10))), list(range(9, -1, -1)))

    def test_all_equal(self):
        self.assertEqual(insertion_sort_decreasing([4, 4, 4, 4]), [4, 4, 4, 4])

    def test_duplicates(self):
        self.assertEqual(insertion_sort_decreasing([3, 1, 3, 2, 1, 3]), [3, 3, 3, 2, 1, 1])

    def test_negatives_and_floats(self):
        self.assertEqual(
            insertion_sort_decreasing([-1.5, 0, 2, -3, 2.5, -1.5]),
            [2.5, 2, 0, -1.5, -1.5, -3],
        )

    def test_strings(self):
        self.assertEqual(
            insertion_sort_decreasing(["pear", "apple", "fig", "banana"]),
            ["pear", "fig", "banana", "apple"],
        )

    # --- contract --------------------------------------------------------

    def test_sorts_in_place_and_returns_same_object(self):
        A = [3, 1, 2]
        result = insertion_sort_decreasing(A)
        self.assertIs(result, A)
        self.assertEqual(A, [3, 2, 1])

    def test_is_a_permutation_of_the_input(self):
        A = [5, 3, 8, 3, 9, 1]
        B = insertion_sort_decreasing(list(A))
        self.assertEqual(sorted(A), sorted(B))

    def test_stable_for_equal_keys(self):
        # Equal keys keep their original relative order because the inner
        # loop uses a strict comparison (A[j] < key), as in the textbook.
        A = [_Keyed(2, "a"), _Keyed(1, "x"), _Keyed(2, "b"), _Keyed(3, "q"), _Keyed(2, "c")]
        insertion_sort_decreasing(A)
        self.assertEqual([x.key for x in A], [3, 2, 2, 2, 1])
        self.assertEqual([x.tag for x in A if x.key == 2], ["a", "b", "c"])

    # --- randomized comparison against the built-in ----------------------

    def test_random_lists_match_builtin_sorted(self):
        rng = random.Random(532)
        for _ in range(300):
            n = rng.randint(0, 40)
            A = [rng.randint(-50, 50) for _ in range(n)]
            expected = sorted(A, reverse=True)
            got = insertion_sort_decreasing(list(A))
            self.assertEqual(got, expected)
            self.assert_monotonically_decreasing(got)


if __name__ == "__main__":
    unittest.main()
