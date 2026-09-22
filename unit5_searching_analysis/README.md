# Unit 5 Discussion: Search Algorithms

## Overview

This assignment compares linear search and binary search.

This program demonstrates and compares linear search and binary search algorithms.
Both algorithms are used to locate a target value in a list and return its index.
If the target is not found, the algorithms return -1.

The program tests both algorithms using small and large datasets, and also demonstrates
edge cases. It also includes a real-world example using student scores.

### How the Algorithms Work

**Linear search** begins at the first element and checks each value one at a time until the 
target is found, or the end of the list is reached. Because linear search may need to 
examine every element, it has O(n) time complexity.

**Binary search** requires the data to be sorted. It checks the middle element and determines
whether the target is in the lower or upper half of the remaining list. The other half is
eliminated from the search. This process continues until the target is found or there are no
values remaining. Because the search space is repeatedly divided in half, binary search has 
O(log n) time complexity.

## Learning Objectives

- Implement linear search
- Implement binary search
- Compare performance
- Analyze algorithm efficiency

## Requirements

1. Test both algorithms on a small dataset.
2. Test both algorithms on a large dataset.
3. Demonstrate edge cases.
4. Analyze performance.
5. Create a real-world search scenario.

## Program Output

For the small dataset, both algorithms returned the same index when the target value was present
and returned -1 when the target was not present.

The large dataset contained 10,000 values. Both algorithms successfully located the target value
9999 at index 9998. However, linear search may need to examine thousands of values to reach a 
target near the end of the list, while binary search repeatedly eliminates half of the remaining
values.

The edge-case tests demonstrated that both algorithms return -1 when searching an empty list. They
also correctly returned index 0 when searching a single-element list containing the target value.

## Real-World Use Case

A school could use a search algorithm to locate a particular score in a collection of student scores.
In this program, both algorithms search a sorted list for a score of 90 and return its location in 
that list. 

Linear search can be used whether the data is sorted. Binary search requires sorted data, but it
can be much more efficient when searching large datasets. This makes binary search useful when large 
amounts of sorted information need to be searched frequently.


