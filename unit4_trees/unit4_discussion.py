"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # A BST node stores its own value plus references to a left
        # child (smaller values) and a right child (larger values).
        # Both children start as None because a new node has no
        # children until something is inserted below it.
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # An empty BST simply has no root node yet. The root will be
        # created the first time insert() is called.
        self.root = None

    def insert(self, value):
        """
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # _insert_recursive returns the (possibly new) subtree root,
        # so we reassign self.root to whatever comes back. On an
        # empty tree this is how the very first node becomes the root.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        # Base case: we've reached an empty spot in the tree, so this
        # is where the new value belongs. Create and return a new node.
        if node is None:
            return Node(value)

        # The BST ordering rule is what makes searching efficient:
        # every value in a node's left subtree is smaller than the
        # node, and every value in its right subtree is larger.
        # We recurse in the direction that preserves that rule.
        if value < node.value:
            # Smaller values always go left.
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            # Larger values always go right.
            node.right = self._insert_recursive(node.right, value)
        # If value == node.value, we treat it as a duplicate and do
        # nothing, leaving the tree unchanged (no duplicate nodes).

        # Return the (unchanged) node reference so the parent call's
        # node.left / node.right assignment reconnects the subtree
        # correctly at every level of the recursion.
        return node

    def search(self, value):
        """
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # Delegate to the recursive helper starting at the root.
        # BST search is typically faster than linear search because
        # at every node we eliminate an entire subtree from
        # consideration (either everything smaller or everything
        # larger) instead of checking one element at a time. On a
        # balanced tree this gives roughly O(log n) search time
        # instead of linear search's O(n).
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        Implement recursive BST search.
        """
        # Base case 1: fell off the tree without finding the value.
        if node is None:
            return False

        # Base case 2: found the value at this node.
        if value == node.value:
            return True

        # Recursive case: use the ordering rule to decide which half
        # of the tree could possibly contain the value, and only
        # search that half — the other half is skipped entirely.
        if value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            # Base case: nothing to visit.
            return

        # In-order traversal produces sorted output in a BST because
        # of the same ordering rule used during insertion: everything
        # in node.left is smaller than node.value, and everything in
        # node.right is larger. Visiting left -> node -> right at
        # every level therefore always outputs values from smallest
        # to largest.
        self._inorder_recursive(node.left, values)   # all smaller values first
        values.append(node.value)                     # then this node
        self._inorder_recursive(node.right, values)   # then all larger values


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # BUILD A TREE
    # ===============================
    print("\n=== TREE CONSTRUCTION ===")

    tree = BST()

    # Insert 7 values that land in both the left and right subtrees
    # of the root. With 50 as the root:
    #   - 30, 20, 40 all go left of 50 (smaller)
    #   - 70, 60, 80 all go right of 50 (larger)
    # Each insert compares against the root first, immediately
    # discarding half the tree from consideration -- that halving of
    # the search space at every level is what makes a BST efficient.
    values_to_insert = [50, 30, 70, 20, 40, 60, 80]

    for v in values_to_insert:
        tree.insert(v)
        print(f"Inserted {v}")

    print(f"\nValues inserted: {values_to_insert}")

    # ===============================
    # IN-ORDER TRAVERSAL
    # ===============================
    print("\n=== IN-ORDER TRAVERSAL ===")

    sorted_values = tree.inorder()
    print(f"In-order traversal result: {sorted_values}")
    print(
        "This comes out sorted because in-order traversal always "
        "visits a node's left subtree (smaller values) before the "
        "node itself, and the node before its right subtree (larger "
        "values) -- and that is exactly how the values were "
        "positioned when they were inserted."
    )

    # ===============================
    # SEARCH TESTS
    # ===============================
    print("\n=== SEARCH TESTS ===")

    # Two values that exist in the tree.
    print(f"Search 40 (exists): {tree.search(40)}")
    print(f"Search 80 (exists): {tree.search(80)}")

    # Two values that do NOT exist in the tree.
    print(f"Search 25 (does not exist): {tree.search(25)}")
    print(f"Search 100 (does not exist): {tree.search(100)}")

    print(
        "Searches for 40 and 80 return True because those values "
        "were inserted earlier. Searches for 25 and 100 return "
        "False: 25 would have to be reached by going left from 50, "
        "left from 30, then right from 20, but that spot is empty "
        "(None), so the recursion hits its base case and returns "
        "False. Similarly, 100 would require going right past 80, "
        "which also has no child there."
    )

    # ===============================
    # EDGE CASES
    # ===============================
    print("\n=== EDGE CASES ===")

    # Edge case 1: searching and traversing an empty tree.
    empty_tree = BST()
    print(f"Search on empty tree: {empty_tree.search(10)}")
    print(f"In-order traversal of empty tree: {empty_tree.inorder()}")
    print(
        "An empty tree has root = None, so _search_recursive and "
        "_inorder_recursive both hit their 'node is None' base case "
        "immediately -- search correctly returns False, and the "
        "traversal correctly returns an empty list, with no errors."
    )

    # Edge case 2: inserting a duplicate value.
    tree.insert(40)  # 40 was already inserted above
    print(f"\nAfter inserting duplicate 40, in-order: {tree.inorder()}")
    print(
        "Inserting 40 again does not change the traversal output: "
        "in _insert_recursive, 40 is neither less than nor greater "
        "than the existing 40 it finds, so neither branch runs and "
        "the tree is left unchanged -- no duplicate node is added."
    )

    # Edge case 3: a tree with only one node.
    single_node_tree = BST()
    single_node_tree.insert(99)
    print(f"\nSingle-node tree in-order: {single_node_tree.inorder()}")
    print(f"Search 99 on single-node tree: {single_node_tree.search(99)}")
    print(f"Search 1 on single-node tree: {single_node_tree.search(1)}")
    print(
        "With only a root node and no children, both left and right "
        "are None, so any search that doesn't match the root value "
        "immediately falls into the 'node is None' base case on the "
        "very next recursive call."
    )


if __name__ == "__main__":
    main()