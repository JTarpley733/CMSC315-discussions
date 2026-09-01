"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Creates empty list that stores the values added to the stack.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Adds the new value to the top of the stack (LIPO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Checks whether the stack is empty before trying to remove a value.
        # Returns None when there is no value because there is no value available to remove.
        if self.is_empty():
            return None

        # Removes and returns the value at the top of the stack,
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Checks whether the stack is empty before trying to access the top value.
        # Returns None when there is no value because there is no value available to view.
        if self.is_empty():
            return None

        # Returns the top value without removing it from the stack.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        # Returns True when the stack contains no values, and False otherwise.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Creates an empty deque to efficiently store values added to the queue.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Adds the new value to the back (right side) of the queue.
        # Oldest value is removed first, supporting FIFO.
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Checks whether the queue is empty before removing a value.
        if self.is_empty():

            # Returns None when there's no value because there is no value available to remove.
            return None

        # Removes and returns the value at the front of the queue.
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Checks whether the queue is empty before accessing the front value.
        if self.is_empty():

            # Returns None when there's no value because there is no value available to view.
            return None

        # Returns the front value without removing it.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        # Returns True when the queue contains no values, and False otherwise.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    print("\n=== STACK DEMO ===")
    # Creates a new empty Stack object.
    stack = Stack()

    # Adds four values to the stack in order.
    # Each new value is placed on top of the previous value.
    stack.push("Apple")
    stack.push("Banana")
    stack.push("Cherry")
    stack.push("Dragon fruit")

    # Prints values added to stack.
    print("\nAdded Apple, Banana, Cherry, and Dragon fruit to the stack.\n")

    # Removes values from the top of the stack.
    # The last value added is the first value removed, demonstrating LIFO.
    print("Removes values from the stack to demonstrate LIFO behavior:")
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())
    print("Popped:", stack.pop())

    # Verifies that all four values have now been removed.
    print("\nIs stack empty?",
    stack.is_empty())

    # Attempts to pop from an empty stack.
    # The pop() method returns None because no values remain.
    print("Attempting to pop from an empty stack:", stack.pop())

    # Attempts to peek at any empty stack.
    # The peek() method returns None because there is no top value.
    print("Attempting to peek at an empty stack:", stack.peek())

    # Creates a separate stack to test the single-item edge case.
    single_stack = Stack()

    # Adds one value and verifies that the stack is not empty.
    single_stack.push("One Item")
    print("\nAdded one item to a new stack.")
    print("Is the single-item stack empty?", single_stack.is_empty())

    # Removes the only item from the stack.
    print("Removed:", single_stack.pop())

    # Verifies that removing the only item leaves the stack empty.
    print("Is the stack empty after removing the only item in it?",
          single_stack.is_empty())


    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.\n")

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    print("=== QUEUE DEMO ===\n")
    # Creates a new empty Queue object.
    queue = Queue()

    # Adds four values to the back of the queue in order. The first value
    # added is the first value removed (FIFO).
    queue.enqueue("Apple")
    queue.enqueue("Banana")
    queue.enqueue("Cherry")
    queue.enqueue("Dragon fruit")

    # Prints statement on values added to the queue.
    print("Added Apple, Banana, Cherry, and Dragon fruit to queue.")

    # Displays the value at the front without removing it
    print("\nValue at the front of the queue:", queue.front())

    # Removes values from the front of the queue. The first value added is
    # the first value removed (FIFO).
    print("\nRemoving values from the queue to demonstrate FIFO:")
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())
    print("Dequeue:", queue.dequeue())

    # Verifies that all four values have been removed.
    print("\nIs the queue empty?", queue.is_empty())

    # Attempts to dequeue from an empty space. Method dequeue() returns None
    # because there is no front value.
    print("\nAttempting to dequeue from an empty queue:", queue.dequeue())

    # Attempts to view the front of an empty queue. Method front() returns None
    # because there is no front value.
    print("Attempting to view the front of an empty queue:", queue.front())

    # Creates a separate queue to test the single-item edge case.
    single_queue = Queue()

    # Adds one value and verifies that the queue is not empty.
    single_queue.enqueue("One Item")
    print("\nAdded one item to a new queue.")
    print("Is the single-item queue empty?", single_queue.is_empty())

    # Removes the only item from the queue.
    print("Removed:", single_queue.dequeue())

    # Verifies that removing the only items leaves the queue empty.
    print("Is the queue empty after removing its only item?", single_queue.is_empty())


    print("\n=== QUEUE DEMO ===")
    print("TODO: Create a Queue object, demonstrate FIFO behavior,")
    print("      test dequeuing from an empty queue,")
    print("      test viewing the front of an empty queue,")
    print("      and verify a single-item queue becomes empty after removal.\n")

if __name__ == "__main__":
    main()
