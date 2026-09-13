"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""

import time


def linear_search(lst, target):
    """
    Implements a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    """
    # Linear search checks every element one at a time, starting
    # at index 0 and moving forward until either a match is found
    # or the end of the list is reached.
    #
    # Time complexity: O(n) — in the worst case (target is at the
    # very end, or not in the list at all), every single element
    # must be checked once. The number of comparisons grows in
    # direct proportion to the size of the list (n), which is
    # exactly what "O(n)" (linear time) means.
    for i in range(len(lst)):
        if lst[i] == target:
            return i  # Found a match — return its position immediately

    # If the loop completes without returning, the target isn't in the list
    return -1


def binary_search(lst, target):
    """
    Implements a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    """
    # Binary search only works correctly on a SORTED list. It takes
    # advantage of that ordering by repeatedly checking the middle
    # element of the current search range and eliminating the half
    # of the list that cannot possibly contain the target.
    low = 0
    high = len(lst) - 1

    while low <= high:
        mid = (low + high) // 2  # Middle index of the current range

        if lst[mid] == target:
            return mid  # Found the target at the middle index

        elif lst[mid] < target:
            # The target must be larger than everything from low..mid,
            # so we can safely discard the entire left half (including mid)
            # and only search the right half from now on.
            low = mid + 1

        else:
            # The target must be smaller than everything from mid..high,
            # so we discard the entire right half (including mid)
            # and only search the left half from now on.
            high = mid - 1

        # Each iteration cuts the remaining search space roughly in half,
        # which is why binary search runs in O(log n) time — for a list
        # of size n, it takes at most about log2(n) comparisons instead
        # of up to n comparisons like linear search.

    # If low crosses past high without finding a match, target isn't present
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================
    print("\n=== SMALL DATASET TEST ===")

    small_dataset = [3, 8, 15, 22, 34, 41, 50, 59, 67, 78]
    print(f"Small dataset: {small_dataset}")

    # --- Test 1: value that exists ---
    existing_value = 41
    linear_result = linear_search(small_dataset, existing_value)
    binary_result = binary_search(small_dataset, existing_value)
    print(f"\nSearching for existing value {existing_value}:")
    print(f"  Linear search result: index {linear_result}")
    print(f"  Binary search result: index {binary_result}")
    # Both algorithms correctly find the value at the same index,
    # confirming that both implementations agree on where 41 lives.

    # --- Test 2: value that does not exist ---
    missing_value = 100
    linear_result = linear_search(small_dataset, missing_value)
    binary_result = binary_search(small_dataset, missing_value)
    print(f"\nSearching for missing value {missing_value}:")
    print(f"  Linear search result: {linear_result}")
    print(f"  Binary search result: {binary_result}")
    # Both return -1 since 100 isn't in the dataset. On a small list
    # like this, the performance difference between the two algorithms
    # is negligible — the dataset is too small to show a meaningful gap.

    # ===============================
    # LARGE DATASET
    # ===============================
    print("\n=== LARGE DATASET TEST ===")