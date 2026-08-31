"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value into the list at the specified index.
    """
    # list.insert() shifts every element from the target index onward
    # one position to the right to make room for the new value.
    # This is necessary because Python lists are stored as contiguous
    # arrays in memory. there's no "gap" to drop a new item into,
    # so everything after the insertion point has to physically move.
    #
    # Performance:
    # - Inserting at the END (index == len(lst)) is fast, O(1) amortized,
    #   because no existing elements need to shift.
    # - Inserting at the BEGINNING or MIDDLE is slower, O(n), because
    #   every element after the insertion point must shift one slot over.
    #   The earlier the index, the more elements have to move.
    lst.insert(index, value)
    return lst


def delete_at(lst, index):
    """
    Remove and return the value at the specified index.
    """
    # Index validation matters because accessing or removing an index
    # that doesn't exist would raise an IndexError and crash the program.
    # Checking bounds first lets us fail gracefully and return None instead,
    # which is safer and more predictable for the caller.
    if index < 0 or index >= len(lst):
        return None

    # list.pop(index) removes the element and returns it in one step.
    # Just like insert, every element after the removed index shifts
    # one position to the LEFT to close the gap so deleting from the
    # beginning or middle is O(n), while deleting the last element
    # (index == len(lst) - 1) is O(1) since nothing needs to shift.
    removed_value = lst.pop(index)
    return removed_value


def search_value(lst, value):
    """
    Search for a value within the list.
    """
    # This is a linear search where we check each element one at a time,
    # starting from index 0, until we either find a match or reach
    # the end of the list. It's called "linear" because the amount of
    # work grows directly (linearly) with the size of the list O(n).
    #
    # We scan sequentially because a plain Python list isn't sorted or
    # indexed by value (unlike a dictionary or set), so there's no way
    # to jump directly to where the value "should" be. Each position
    # must be checked individually.
    for i in range(len(lst)):
        if lst[i] == value:
            return i
    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================
    print("\n=== INSERTION TESTS ===")

    # 1. Create a list containing several values.
    numbers = [10, 20, 30, 40, 50]

    # 2. Display the original list.
    print("Original list:", numbers)

    # 3. Test insertion at the beginning.
    # Inserting at index 0 forces every existing element to shift right
    # by one, so this is the most expensive insertion position, O(n).
    insert_at(numbers, 0, 5)
    print("After inserting 5 at the beginning:", numbers)

    # Test insertion in the middle.
    # Only the elements from the middle index onward need to shift,
    # so it's still O(n) but touches fewer elements than inserting at 0.
    middle_index = len(numbers) // 2
    insert_at(numbers, middle_index, 99)
    print(f"After inserting 99 at the middle (index {middle_index}):", numbers)

    # Test insertion at the end.
    # No elements need to shift here, so this is the cheapest case, O(1) amortized.
    insert_at(numbers, len(numbers), 100)
    print("After inserting 100 at the end:", numbers)

    # ===============================
    # DELETION TESTS
    # ===============================
    print("\n=== DELETION TESTS ===")

    # Delete from the beginning.
    # Removing index 0 shifts every remaining element left by one, O(n).
    removed = delete_at(numbers, 0)
    print(f"Removed value from the beginning: {removed}")
    print("List after deletion:", numbers)

    # Delete from the middle.
    middle_index = len(numbers) // 2
    removed = delete_at(numbers, middle_index)
    print(f"Removed value from the middle (index {middle_index}): {removed}")
    print("List after deletion:", numbers)

    # Delete from the end.
    # No shifting required since nothing comes after the last element, O(1).
    removed = delete_at(numbers, len(numbers) - 1)
    print(f"Removed value from the end: {removed}")
    print("List after deletion:", numbers)

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")

    # Search for a value that exists.
    target = numbers[1] if len(numbers) > 1 else numbers[0]
    result = search_value(numbers, target)
    print(f"Searching for {target} (exists): found at index {result}")

    # Search for a value that does not exist.
    missing_value = 9999
    result = search_value(numbers, missing_value)
    print(f"Searching for {missing_value} (does not exist): result {result} (-1 means not found)")

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge case 1: Delete using an invalid index.
    # Our delete_at() checks bounds first and returns None instead of
    # crashing with an IndexError.
    invalid_index = 999
    result = delete_at(numbers, invalid_index)
    print(f"Deleting at invalid index {invalid_index}: result = {result} (safely handled)")

    # Edge case 2: Insert into an empty list.
    # Inserting into an empty list at index 0 (or any index) simply
    # places the value as the only element -- there's nothing to shift.
    empty_list = []
    insert_at(empty_list, 0, 42)
    print("Inserting 42 into an empty list:", empty_list)

    # Edge case 3 (bonus): Delete from an empty list.
    # Bounds check catches this immediately since len([]) == 0, so any
    # index is out of range, and we safely return None.
    empty_list_2 = []
    result = delete_at(empty_list_2, 0)
    print(f"Deleting from an empty list: result = {result} (safely handled)")

    # Edge case 4 (bonus): Search for a value in an empty list.
    # The loop in search_value() never executes since range(0) is empty,
    # so it falls through to return -1 immediately.
    result = search_value(empty_list_2, 42)
    print(f"Searching an empty list for 42: result = {result} (-1 means not found)")


if __name__ == "__main__":
    main()