# Unit 3 Discussion: List Operations

## Overview

This assignment examines insertion, deletion, and searching in Python lists. It demonstrates how
Python lists can be used to store, organize, and manipulate data. This program implements three 
common list operations, tests these three operations at different positions in a list, 
demonstrates edge cases, and applies the concepts to a real-world scenario.


### List Structure and Algorithms
Python lists are ordered collections that allow elements to be accessed using an index. The first
element is located at index 0, and each subsequent element has the next sequential index.

#### Insertion
The _insert_at()_ function uses Python's _insert()_ method to place a value at a specified index. 
When an item is inserted at the beginning or middle of a list, existing elements at and after that
position are shifted to the right to make room for the new element. IInserting at the end generally
requires less shifting than inserting near the beginning.

This program demonstrates insertion at the beginning, middle, and end of a list.

#### Deletion
The _delete_at()_ function first checks whether the requested index is valid. If valid, the _pop()_
method removes and returns the element at that index. Elements following the deleted value shift to
the left to fill the empty position. If the index is invalid, the function returns _None_. This 
validation prevents the program from attempting to access a position that does not exist and avoids
an _IndexError_.

This program tests deletion from the beginning, middle, and end of the list.

#### Linear Search
The _search_value()_ function uses a linear search algorithm. It begins with the first element and 
compares each value sequentially with the requested value. If a match is found, the function returns
its index. If the entire list is searched without finding a match, the function returns -1.



## Learning Objectives

- Insert values into a list
- Delete values from a list
- Search for values in a list
- Analyze list behavior and performance

## Requirements

1. Test insertion at the beginning, middle, and end.
2. Test deletion at the beginning, middle, and end.
3. Search for existing and missing values.
4. Demonstrate edge cases.
5. Create a real-world scenario.

## Program Output

The output demonstrates how each operation changes the list. During the insertion tests, new values
are added at the beginning, middle, and end, and the updated list is displayed after each operation. 
The deletion tests show both the value removed and the resulting list.

The search tests demonstrate two possible results. Searching for an existing value returns its index, 
while searching for a value that is not present returns -1.

This program also demonstrates several edge cases. Attempting to delete an invalid index or delete from
an empty list safely returns _None_. The program also demonstrates inserting into an empty list and 
removing the only item from a single-item list. These tests show that the functions can handle unusual
conditions without causing the program to fail.

## Real-World Use Case

A streaming service's viewing history is used as a real-world example of a list. Each show represents an 
item stored in the user's viewer history. When another show is watched, it can be inserted into the list.
If a show was recorded incorrectly, it can be removed.The application can also search the list to 
determine whether a particular show appears in the viewing history.

This scenario demonstrated why list operations are useful in real applications. Lists maintain the order
of stored data while allowing applications to insert, removed, retrieve, and search for information as 
the data changes. 