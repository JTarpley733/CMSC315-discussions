# Unit 4 Discussion: Binary Search Trees

## Overview

This assignment introduces Binary Search Trees (BSTs) and recursive tree operations.
It demonstrates how a Binary Search Tree can be used to organize, search, and traverse data.
Each node in the tree stores a value and references to a left and right child. Values smaller
than the current node are placed in the left subtree, while values larger than the current node
are placed in the right subtree.

This program uses recursion to insert values, search for values, and perform an in-order 
traversal of the tree.

### How the Binary Search Tree Works

The program creates a BST and inserts the values:
60, 40, 80, 20, 50, 70, 100

The resulting tree has the following structure:

                 60
                /  \
              40   80
             / \   / \
            20 50 70 100

When a value is inserted, the program compares it with the current node. A smaller value moves
to the left subtree, while a larger value moves to the right subtree. This process continues 
recursively until an empty position is found.

Searching works in a similar way. Instead of checking every value sequentially, the BST uses
comparisons to determine which subtree could contain the target. In a reasonably balanced BST, 
thus produces the values in ascending order.

## Learning Objectives

- Build a BST
- Insert values recursively
- Search recursively
- Perform in-order traversal
- Understand BST organization

## Requirements

1. Build a BST.
2. Insert multiple values.
3. Demonstrate in-order traversal.
4. Test searching.
5. Demonstrate edge cases.
6. Create a real-world BST example.

## Program Output

The in-order traversal produces:

[60, 40, 80, 20, 50, 70, 100]

This demonstrates that the BST correctly organized the inserted values and that the in-order traversal
returned them in sorted order.

This program also searches for values that are present and absent from the tree. Searching for 40 and 60
returns True because these values exist in the BST. Searching for the values 10 and 30 returns False because
they were not inserted.

An empty BST is also created and tested as an edge case. Traversing the empty tree returns an empty list 
because there are no nodes to visit. Searching the empty tree returns False because there is no roor node 
or other value to search.

## Real-World Use Case

One example of a real-world use for a BST is maintaining a searchable collection of records. For example, a
veterinary hospital could use a tree structure to organize patient identification numbers. When searching 
for a particular patient ID, comparisons could determine whether to continue searching values that are smaller
or larger than the currny value instead of checking every record sequentially.

This demonstrates how tree-based data structures can help organize information while supporting efficient 
searching.

