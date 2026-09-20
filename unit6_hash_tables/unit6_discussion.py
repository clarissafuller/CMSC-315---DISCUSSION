"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE
    # ===============================
    #
    # A Python dictionary IS a hash table under the hood: each key is
    # run through a hash function to produce an integer hash code, and
    # that hash code determines which "bucket" the key-value pair is
    # stored in internally. This is why dictionary lookups, inserts,
    # and deletes run in average O(1) time instead of having to scan
    # every item like a list would.
    #
    # Keys must be hashable (immutable types like strings, numbers,
    # and tuples work; lists and dicts cannot be keys because their
    # contents - and therefore their hash - could change).

    inventory = {}  # empty dictionary / hash table

    inventory["P100"] = 15
    inventory["P200"] = 9
    inventory["P300"] = 42
    inventory["P400"] = 3
    inventory["P500"] = 27

    print("\n=== INSERT OPERATIONS ===")
    # Each assignment above hashes the string key ("P100", "P200", etc.)
    # to determine where the pair is stored. Insertion order is not
    # what determines storage location - the hash value is.
    print("Dictionary after inserting 5 key-value pairs:")
    print(inventory)

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================
    print("\n=== LOOKUP OPERATIONS ===")
    # A lookup re-hashes the key and jumps almost directly to the
    # bucket where the value lives, rather than searching sequentially.
    print(f"Quantity for P100: {inventory['P100']}")
    print(f"Quantity for P300: {inventory['P300']}")

    # ===============================
    # UPDATE OPERATIONS
    # ===============================
    print("\n=== UPDATE OPERATIONS ===")
    print("Dictionary BEFORE update:")
    print(inventory)

    # Assigning to an existing key does not create a new entry - the
    # key hashes to the same bucket it already occupies, so the old
    # value is simply overwritten in place. The dictionary's size
    # does not change.
    inventory["P100"] = 50

    print("Dictionary AFTER updating P100 to 50:")
    print(inventory)

    # ===============================
    # DELETE OPERATIONS
    # ===============================
    print("\n=== DELETE OPERATIONS ===")
    print("Dictionary BEFORE deletion:")
    print(inventory)

    # del removes the key-value pair entirely - the key is un-hashed
    # from its bucket and the space becomes available for a future
    # key that happens to hash to the same location.
    del inventory["P400"]

    print("Dictionary AFTER deleting key 'P400':")
    print(inventory)

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge case 1: looking up a key that does not exist.
    # Using [] directly would raise a KeyError, so .get() is used
    # instead, which returns None (or a default) when the key is
    # missing rather than crashing the program.
    missing_lookup = inventory.get("P999")
    print(f"Lookup missing key 'P999' with .get(): {missing_lookup}")

    # Edge case 2: deleting a key that does not exist.
    # del on a missing key raises a KeyError, so checking membership
    # first (or using .pop(key, None)) avoids crashing the program.
    if "P999" in inventory:
        del inventory["P999"]
        print("Deleted 'P999'")
    else:
        print("Attempted to delete missing key 'P999' - handled safely, no crash")

    # Edge case 3: updating/inserting into an empty dictionary.
    # There is no error here - assigning to a new key on an empty
    # dict simply creates the first entry, same as any other insert.
    empty_dict = {}
    empty_dict["NEW1"] = 100
    print(f"Assigned into an empty dictionary: {empty_dict}")

    # Edge case 4: checking membership on an empty dictionary.
    # This is always False and never raises an error - it's a safe,
    # cheap operation regardless of dictionary size.
    print(f"Is 'ANY_KEY' in empty_dict? {'ANY_KEY' in empty_dict}")


if __name__ == "__main__":
    main()