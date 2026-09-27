"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    Sort a list using Bubble Sort and return a new sorted list.

    Bubble Sort repeatedly steps through the list, compares adjacent
    elements, and swaps them if they are out of order. After each pass,
    the largest unsorted value "bubbles" to its final position at the end.

    Time complexity: O(n^2) worst/average case, O(n) best case
    (already sorted, thanks to the early-exit check).
    Space complexity: O(n) here because we copy the list; the sort
    itself works in place.
    """
    # Copy the list so the original is not modified.
    result = lst.copy()
    n = len(result)

    # Each pass places the next-largest value at the end of the list.
    for i in range(n - 1):
        swapped = False

        # The last i elements are already in their final positions,
        # so each pass can stop earlier than the one before it.
        for j in range(n - 1 - i):
            # Swap adjacent elements if they are out of order.
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True

        # If a full pass made no swaps, the list is already sorted.
        if not swapped:
            break

    return result


def merge_sort(lst):
    """
    Sort a list using Merge Sort and return a new sorted list.

    Merge Sort is a divide-and-conquer algorithm: it splits the list
    in half, recursively sorts each half, and then merges the two
    sorted halves back together.

    Time complexity: O(n log n) in all cases.
    Space complexity: O(n) for the temporary lists created while merging.
    """
    # Base case: a list with 0 or 1 elements is already sorted.
    # Returning a copy keeps the original list unmodified.
    if len(lst) <= 1:
        return lst.copy()

    # Divide: find the middle and split the list into two halves.
    mid = len(lst) // 2
    left_half = lst[:mid]
    right_half = lst[mid:]

    # Conquer: recursively sort each half.
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Combine: merge the two sorted halves into one sorted list.
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    Merge two already-sorted lists into a single sorted list.
    """
    result = []
    i = 0  # Current position in the left list
    j = 0  # Current position in the right list

    # Compare the front values of each list and take the smaller one.
    # Using <= keeps equal values in their original order (a stable sort).
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # One list has run out. The other's remaining values are already
    # sorted and larger than everything in result, so append them as-is.
    result.extend(left[i:])
    result.extend(right[j:])

    return result


def run_both(label, data):
    """Sort a dataset with both algorithms and display labeled results."""
    bubble_result = bubble_sort(data)
    merge_result = merge_sort(data)

    print(f"\n{label}")
    print(f"  Original:    {data}")
    print(f"  Bubble Sort: {bubble_result}")
    print(f"  Merge Sort:  {merge_result}")
    print(f"  Results match: {bubble_result == merge_result}")


def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # DATASET #1
    # ===============================
    print("\n=== DATASET #1 ===")
    dataset1 = [64, 34, 25, 12, 22, 11, 90, 5]
    run_both("Unsorted integers:", dataset1)
    print(f"  Original unchanged: {dataset1}")

    # ===============================
    # DATASET #2
    # ===============================
    print("\n=== DATASET #2 ===")
    dataset2 = [3.7, -8, 15, 0, 42, -2.5, 19, 7, 1]
    run_both("Mixed negatives, zero, and decimals:", dataset2)
    print("  Both algorithms produce the same sorted order. They differ in")
    print("  efficiency: Bubble Sort makes O(n^2) comparisons, while Merge")
    print("  Sort makes O(n log n), which matters more as lists grow.")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASE TESTS ===")

    run_both("Empty list:", [])
    print("  Nothing to compare. Bubble Sort's loops never run, and Merge")
    print("  Sort hits its base case right away. Both return [].")

    run_both("Single-element list:", [42])
    print("  One element is already sorted. Merge Sort returns at the base")
    print("  case, and Bubble Sort has no adjacent pairs to compare.")

    run_both("Already sorted list:", [1, 2, 3, 4, 5, 6, 7])
    print("  Bubble Sort's best case: the first pass makes no swaps, so the")
    print("  early exit stops it after one pass (O(n)). Merge Sort still")
    print("  splits and merges every level, so it stays O(n log n).")

    run_both("Reverse-sorted list:", [9, 8, 7, 6, 5, 4, 3, 2, 1])
    print("  Bubble Sort's worst case: every adjacent pair is out of order,")
    print("  so it swaps on every comparison (O(n^2)). Merge Sort does the")
    print("  same amount of work as for any other input.")

    run_both("List with duplicates:", [5, 3, 8, 3, 1, 5, 8, 1])
    print("  Duplicates are kept, not removed. Bubble Sort only swaps when")
    print("  a value is strictly greater, and merge() uses <=, so equal")
    print("  values keep their relative order. Both sorts are stable.")


if __name__ == "__main__":
    main()