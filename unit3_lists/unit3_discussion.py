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
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """
    # The insert() method places the new value at the specified index.
    # Existing value at specified index are shifted to the right by one position.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """
    # Checks whether the index refers to an existing value in the list.
    # Validation prevents an IndexError from occurring.
    if index < 0 or index >= len(lst):
        return None

    # Removes the element at the specified index and returns its value.
    # Values located after the removed item shift one position to the left.
    removed_value = lst.pop(index)

    # Returns the removed value. Allows program to display or use it later.
    return removed_value


def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """
    # Checks one for specified value, one element at a time, until value is found.
    for index in range(len(lst)):

        # Compares current list element with requested value.
        if lst[index] == value:
            return index

    # Returns -1 to indicate that the value was not found.
    return -1


def main():
    print("UNIT 3: LIST OPERATIONS")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================

    print("\n=== INSERTION TESTS ===")
    print("TODO: Create a list and demonstrate insertions.\n")

    # 1. Creates a starting list containing a few values.
    numbers = [25, 50, 75, 100]

    # 2. Displays the list before any insertion operation is performed.
    print("Original list:", numbers)

    # 3-5. Tests insertion at the beginning by inserting 5 at index 0.
    insert_at(numbers, 0, 5)
    print("Updated list after inserting 5 at the beginning:", numbers)

    # Tests insertion in the middle by inserting 2 at index 3.
    insert_at(numbers, 2, 15)
    print("Updated list after inserting 15 in the middle:", numbers)

    # Tests insertion at the end by using len(numbers) to insert 20 at the end.
    insert_at(numbers, len(numbers), 20)
    print("Updated list after inserting 20 at the end:", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================

    print("\n=== DELETION TESTS ===")
    print("TODO: Demonstrate deletions from multiple positions.\n")

    # 1-4. Deletes item from the beginning by removing the value at index 0.
    #      Displays removed value and updated list after deletion.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("Updated list after beginning deletion:", numbers)

    # Deletes element from thd middle of the list by removing value at index 2.
    # Displays removed value and updated list after deletion.
    removed = delete_at(numbers,2)
    print("Removed from middle:", removed)
    print("Updated list after middle deletion:", numbers)

    # Deletes element from the end of the list by using len(numbers) to delete
    # value at the end. -1 Represents index of the last element.
    # Displays removed value and updated list after deletion.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("Updated list after end deletion:", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")
    print("TODO: Demonstrate searching for values.\n")

    # 1-4. Searches for a value that exists in the list.
    # Displays search result with index.
    existing_value = 75
    result = search_value(numbers, existing_value)
    print(existing_value, "is located at index:", result)

    # Searches for a value that does not exist in the list.
    # Displays search result.
    missing_value = 99
    result = search_value(numbers, missing_value)
    print(missing_value, "search result:", result)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate at least two edge cases.\n")

    # Edge case 1:
    # Creates an empty list and inserts a value into it.
    # Displays updated list with added value.
    print("Edge case 1: Creates an empty list, then inserts a value into it.")
    empty_list = []
    print("Empty list:", empty_list)
    insert_at(empty_list, 0, 125)
    print("Updated list after inserting into an empty list:", empty_list)

    # Edge case 2:
    # Attempts to delete from an empty list.
    # Displays message after attempting to delete from empty list.
    print("\nEdge case 2: Attempts to delete from an empty list.")
    removed = delete_at(empty_list, 0)
    print("Attempted to delete value from empty list:", removed)

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================
    print("\n===============================")
    print("REAL-WORLD SCENARIO")
    print("===============================\n")

    # A streaming service, such as HULU, could use a list to store a user's viewing history.
    print("A streaming service, such as HULU, could use a list to store a user's viewing history.")
    print("Example follows:\n")

    viewing_history = [
        "Stranger Things",
        "King of the Hill",
        "Gilmore Girls"
    ]

    # Displays viewing history.
    print("Your viewing history", viewing_history)

    # A currently watched show is added to the end of the viewing history.
    # Displays updated viewing history after insertion.
    insert_at(viewing_history, len(viewing_history), "The Simpsons")
    print("Your updated viewing history:", viewing_history)

    # A show mistakenly clicked on is removed from the viewing history.
    # Displays updated list after deletion.
    removed_show = delete_at(viewing_history, 1)
    print("Removed from your viewing history:", removed_show)
    print("Your updated viewing history:", viewing_history)

    # Searches the viewing history to determine whether a specified show was watched.
    # Checks for index, displays index if True, displays "not found" if False.
    # Displays results of search.
    show_to_find = "American Horror Story"
    position = search_value(viewing_history, show_to_find)

    if position != -1:
        print(show_to_find, "was found at index", position)
    else:
        print(show_to_find, "was not found in your viewing history.")

if __name__ == "__main__":
    main()