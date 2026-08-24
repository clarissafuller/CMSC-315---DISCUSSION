Unit 2 Discussion: Stacks and Queues
Overview

This assignment explores two fundamental linear data structures:

Stack (LIFO)
Queue (FIFO)
Learning Objectives
Implement stack operations
Implement queue operations
Understand LIFO and FIFO behavior
Create edge cases
Requirements

Complete all TODO sections:

Implement stack operations.
Implement queue operations.
Demonstrate LIFO behavior.
Demonstrate FIFO behavior.
Create and test edge cases.
Create a real-world scenario.
Implementation Notes
Stack and Queue Classes

Implemented both the Stack and Queue classes:

Stack used a Python list as its internal structure, with push(), pop(), peek(), and is_empty(). pop() and peek() raised an IndexError when called on an empty stack. Comments were added explaining how appending/removing from the end of the list produces LIFO behavior.
Queue used a collections.deque as its internal structure, with enqueue(), dequeue(), front(), and is_empty(). dequeue() and front() raised an IndexError when called on an empty queue. Comments were added explaining how adding to the back and removing from the front produces FIFO behavior.
Queue Demo

Completed the queue demo in main():

Created a Queue object and enqueued four values (10, 20, 30, 40), printing the front of the queue after each addition.
Demonstrated FIFO behavior by dequeuing all values and confirming they came out in the same order they were added.
Tested the edge case of calling dequeue() on an empty queue and caught the resulting error.
Tested the edge case of calling front() on an empty queue and caught the resulting error.
Created a single-item queue, verified it was not empty, removed the item, and confirmed is_empty() returned True afterward.

All print statements were rewritten to clearly explain each step of the demo as it ran.

Real-World Scenario

Added a real-world scenario using the Queue class: a coffee shop mobile order line.

Four customer orders were enqueued in the order they were placed.
The barista then dequeued and "served" each order one at a time, confirming customers were served in the exact order they arrived.
The scenario explained why a Queue (FIFO) — rather than a Stack (LIFO) — is the correct structure here: a Stack would serve the most recent customer first, which would not be fair or realistic for an order line.
Outstanding Work
Stack demo: Not yet implemented. The file's main() still only contains the stack demo's TODO comments and placeholder print statements — no Stack object is created or exercised. The stack demo still needs to create a Stack, push at least four values, demonstrate LIFO behavior, and test the same two edge cases (pop() and peek() on an empty stack, plus a single-item stack).
Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

What concepts or skills did you learn while completing this assignment?
What challenges did you encounter, and how did you overcome them?
Explain the differences between stacks and queues as this relates to real-world applications.