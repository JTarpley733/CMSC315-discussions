# Unit 2 Discussion: Stacks and Queues

## Overview

This assignment explores two fundamental linear data structures:

- Stack (LIFO)
- Queue (FIFO)

The stack follows the Last-In, First-Out (LIFO) principle. 
Values were added to the top of the stack using _push()_ and removed
from the top using _pop()_. Therefore, the most recently added value is
always the first one removed. The _peek()_ method allows the top value to
be viewed without removing it.

The queue follows the First-In, First-Out (FIFO) principle. Values were 
added to the back of the queue using _enqueue()_ and removed from the front 
using _dequeue()_. This ensured that the values were processed in the same
order in which they were added. The _front()_ method allowed the first value 
to be viewed without removing it.


## Learning Objectives

- Implement stack operations
- Implement queue operations
- Understand LIFO and FIFO behavior
- Create edge cases
- Understand practical applications of stacks and queues.

## Requirements

Complete all TODO sections:

1. Implement stack operations.
2. Implement queue operations.
3. Demonstrate LIFO behavior.
4. Demonstrate FIFO behavior.
5. Create and test edge cases.
6. Create a real-world scenario.

## Real-World Applications

Stacks can be implemented for operations that need to be completed in reverse 
order, while queues are useful when items need to be processed in the order in
which they arrive. One common example using a stack is the **Undo feature** in
a text editor. Each action can be pushed onto a stack as it occures, so when the
user selects Undo, the most recent action is removed first while additional undo 
operations continue working backward through the previous actions. An example 
using a queue is a customer service (CRM) or technical support (TSS) system.
Requests can be added to a queue as customers submit them, and the oldest request
is pushed to the top so it can be handled first. This provides an orderly method 
for processing requests based on arrival time.
