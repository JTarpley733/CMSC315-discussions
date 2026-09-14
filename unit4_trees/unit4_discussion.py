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
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        # Stores the value held by this node.
        self.value = value

        # Each new node begins without any child nodes.
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        # An empty BST does not have a root node yet.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        # The recursive helper begins searching for the correct insertion
        # position starting at the root.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # If this position is empty, a new node can be created here.
        if node is None:
            return Node(value)

        # In a BST, values smaller than the current node belong in the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Values larger than the current node belong in the right subtree.
        elif value > node.value:
            node.right =  self._insert_recursive(node.right, value)

        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        # BST searching can often be faster than linear search because each
        # comparison can eliminate an entire subtree from consideration.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # If the search reaches an empty position, the value is not present.
        if node is None:
            return False

        # If the current node holds the target value, the search succeeds.
        if value == node.value:
            return True

        # If the target value is smaller, only the left subtree is searched.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # If the target value is larger, the right subtree is searched.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        # Creates list to store each value in traversal order.
        values = []

        # Initiates the recursive traversal at the root.
        self._inorder_recursive(self.root, values)

        # Returns the completed traversal list.
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        # BST values are organized with smaller values on the left and larger
        # values on the right so that visiting left-node-right produces the values
        # in sorted ascending order.

        # If a null node has no value to visit, recursion will stop here.
        if node is None:
            return

        # All smaller values in the left subtree are visited recursively first.
        self._inorder_recursive(node.left, values)

        # Visits current node.
        values.append(node.value)

        # All larger values in the right subtree are visited recursively last.
        self._inorder_recursive(node.right, values)


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    print("TODO: Create a BST and insert multiple values.")

    # Creates an empty Binary Search Tree.
    tree = BST()

    # Creates nodes on both the left and right side of root node for these values to be inserted into.
    values_to_insert = [60, 40, 80, 20, 50, 70, 100]

    # Inserts each value into the BST.
    for value in values_to_insert:
        tree.insert(value)

    # Displays BST. A BST reduces the search space because each comparison determines whether the next
    # step should continue into the left or right subtree, instead of checking every value sequentially.
    print("Values inserted:", values_to_insert)

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")
    print("TODO: Display and explain traversal results.")

    # In-order traversal visits the left subtree, then the current node, then the right subtree.
    # Since BST nodes are arranged by value, this produces the values in ascending sorted order.
    traversal_result = tree.inorder()

    # Displays results.
    print("In-order traversal:", traversal_result)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate BST searching.")

    # Search() returns True because these values exist in the tree.
    print("Search for 40:", tree.search(40))
    print("Search for 60:", tree.search(60))

    # Search() returns False because these values are NOT in the tree.
    print("Search for 10:", tree.search(10))
    print("Search for 30:", tree.search(30))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain an edge case.")

    # Creates an empty Binary Search Tree.
    empty_tree = BST()

    # Returns an empty list and displays it.
    # Traversing an empty tree returns an empty list because there are no nodes for
    # the recursive traversal to visit.
    print("Empty tree traversal:", empty_tree.inorder())

    # Searches empty tree for value, returns False because the root is None.
    print("Search empty tree for 40:", empty_tree.search(40))



if __name__ == "__main__":
    main()