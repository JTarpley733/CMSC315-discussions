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


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    # Checks each value in the list one at a time, beginning at index 0.
    for index in range(len(lst)):

        # If the current value matches the target, its index is returned.
        if lst[index] == target:
            return index

    # Linear search has an O9n) time complexity because, in the worst case,
    # every element in the list may need to be checked.

    # Returns -1 if the entire list is searched without finding the target.
    return -1


def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    # Sets the beginning and ending boundaries of the search.
    low = 0
    high = len(lst) - 1

    # Continues searching while there are still values to examine.
    while low <= high:

        # Finds the middle index of the current search range.
        mid = low + (high - low) // 2

        # Returns the middle index if its value matches the target.
        if lst[mid] == target:
            return mid

        # If the target is smaller than the middle value, the upper
        # half can be eliminated from the search.
        elif target < lst[mid]:
            high = mid - 1

        # If the target is larger than the middle value, the lower half
        # can be eliminated from the search.
        else:
            low = mid + 1

            # Each iteration eliminates approximately half of the remaining
            # values, giving binary search O(log n) time complexity on a sorted
            # list.

    # Returns -1 if the target is not found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")
    print("TODO: Create a small dataset and test both searches.")

    # Creates a small sorted dataset of student scores.
    small_scores = [65, 77, 81, 82, 92, 95]

    # Searches for 81, which exists at index 2. Both algorithms should return
    # the same index.
    print("Linear search for 81:", linear_search(small_scores, 81))
    print("Binary search for 81:", binary_search(small_scores, 81))

    # Searches for 92, which is not in the list.. Both algorithms should return
    # -1 .
    print("Linear search for 90:", linear_search(small_scores, 90))
    print("Binary search for 90:", binary_search(small_scores, 90))

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")
    print("TODO: Create a larger dataset and compare results.")

    # Linear search may need to examine thousands of elements to find a value
    # near the end of the list. Binary search repeatedly cuts the remaining
    # search area in half, making the difference in efficiency more significant
    # as the dataset becomes larger.

    # Creates a sorted list containing 10,000 values from 1 to 10,000
    large_dataset = list(range(1, 10001))

    # Searches for a value near the end of the larget dataset.
    large_target = 9999

    # Both algorithms should find the same value at index 9999
    print("Linear search for 9999:", linear_search(large_dataset, large_target))
    print("Binary search for 9999:", binary_search(large_dataset, large_target))

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge Case 1: Empty List.
    # Neither algorithm has any values to examine, so both return -1.
    empty_list = []

    print("Linear search empty list:", linear_search(empty_list, 60))
    print("Binary search empty list:", binary_search(empty_list, 60))

    # Edge Case 2: Single-element list.
    # The only value matches the target, so both searches return an index of 0.
    single_value = [95]

    print("Linear search for single-element list:", linear_search(single_value, 95))
    print("Binary search for single-element list:", binary_search(single_value, 95))

    print("\n=== REAL-WORD DATASET SCENARIO ===")

    # A school needs a way to store student scores. This school could store the student scores in
    # a list and search for a particular score when needed. If the scores are sorted, binary search
    # can efficiently reduce the number of values that must be examined.

    student_scores = [60, 65, 70, 75, 80, 85, 90, 95, 100]
    target_score = 90

    # Searches the student score list using both algorithms.
    linear_result = linear_search(student_scores, target_score)
    binary_result = binary_search(student_scores, target_score)

    # Displays the index returned by each search algorithm.
    print("Student scores:", student_scores)
    print("Target score:", target_score)
    print("Linear search result:", linear_result)
    print("Binary search result:", binary_result)


if __name__ == "__main__":
    main()