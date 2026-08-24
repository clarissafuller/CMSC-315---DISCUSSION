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
        # Hint: A Python list can be used to store stack values.
        self._stack = []
 
    def push(self, value):
        # TODO (Student): Add value to the stack.
        # A list's append() adds to the end, which we treat as the "top"
        # of the stack — so the most recently pushed value is always
        # the next one out. This is what gives a stack its LIFO behavior.
        self._stack.append(value)
 
    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # If the stack is empty, there is nothing to remove, so an
        # IndexError is raised instead of silently returning None.
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._stack.pop()
 
    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # peek() lets you look at the next value that would be popped
        # without actually changing the contents of the stack.
        if self.is_empty():
            raise IndexError("peek at empty stack")
        return self._stack[-1]
 
    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self._stack) == 0
 
 
class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self._queue = deque()
 
    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # append() always adds to the right/back end of the deque, so
        # values keep their original order — the first one added is
        # still the first one that will come out. This gives FIFO behavior.
        self._queue.append(value)
 
    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # popleft() removes from the front (left end) of the deque, which
        # is what makes this FIFO instead of LIFO. If the queue is empty,
        # an IndexError is raised.
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._queue.popleft()
 
    def front(self):
        # TODO (Student): Return the front value without removing it.
        # front() returns the next value that would be dequeued, without
        # removing it from the queue.
        if self.is_empty():
            raise IndexError("front of empty queue")
        return self._queue[0]
 
    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self._queue) == 0
 
 
def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
 
    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.
 
    print("\n=== STACK DEMO ===")
    print("TODO: Create a Stack object, demonstrate LIFO behavior,")
    print("      test popping from an empty stack,")
    print("      test peeking at an empty stack,")
    print("      and verify a single-item stack becomes empty after removal.")
 
    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.
 
    print("\n=== QUEUE DEMO ===")
 
    print("\n--- Building the Queue ---")
    numQueue = Queue()
    values_to_add = [10, 20, 30, 40]
 
    for value in values_to_add:
        numQueue.enqueue(value)
        print(f"Enqueued {value}. Front of queue is now: {numQueue.front()}")
 
    print("\n--- Demonstrating FIFO (First In, First Out) Behavior ---")
    print("We added values in this order: 10, 20, 30, 40")
    print("Because a queue is FIFO, they should come back out in the SAME order.\n")
 
    while not numQueue.is_empty():
        removed = numQueue.dequeue()
        print(f"Dequeued: {removed}")
 
    print("All values removed in the order they were added — FIFO confirmed.")
 
    print("\n--- Edge Case: Dequeuing from an Empty Queue ---")
    print("The queue is currently empty. Attempting to dequeue anyway...")
    try:
        numQueue.dequeue()
    except Exception as e:
        print(f"As expected, this raised an error: {e}")
 
    print("\n--- Edge Case: Viewing the Front of an Empty Queue ---")
    print("The queue is still empty. Attempting to view the front item...")
    try:
        numQueue.front()
    except Exception as e:
        print(f"As expected, this raised an error: {e}")
 
    print("\n--- Edge Case: Single-Item Queue ---")
    singleQueue = Queue()
    singleQueue.enqueue(99)
    print("Created a new queue and enqueued a single value: 99")
    print(f"Is the queue empty right now? {singleQueue.is_empty()}")
 
    removed = singleQueue.dequeue()
    print(f"Dequeued the only item: {removed}")
    print(f"Is the queue empty now? {singleQueue.is_empty()}")
 
    print("\n=== END OF QUEUE DEMO ===\n")
 
    # ===============================
    # TODO (Student): REAL-WORLD SCENARIO
    # ===============================
    # Requirement 6: Create a real-world scenario.
    #
    # Scenario: a coffee shop's mobile order line.
    # Customers place orders and are served in the exact order they
    # arrived — the first person to order is the first person served.
    # This is a natural fit for a Queue (FIFO), since a Stack (LIFO)
    # would mean the LAST customer to order gets served FIRST, which
    # would not be fair or realistic for a real order line.
 
    print("=== REAL-WORLD SCENARIO: COFFEE SHOP ORDER LINE ===")
    print("Customers are served in the order they placed their orders (FIFO).\n")
 
    order_line = Queue()
    customer_orders = [
        "Order #1: Maya - Latte",
        "Order #2: Devon - Cold Brew",
        "Order #3: Priya - Cappuccino",
        "Order #4: Sam - Drip Coffee",
    ]
 
    print("--- Customers Placing Orders ---")
    for order in customer_orders:
        order_line.enqueue(order)
        print(f"Order placed and added to the line: {order}")
 
    print(f"\nNext order up: {order_line.front()}")
 
    print("\n--- Barista Serving Orders ---")
    while not order_line.is_empty():
        current_order = order_line.dequeue()
        print(f"Now serving: {current_order}")
 
    print("\nAll customers have been served in the order they arrived.")
    print("This confirms a Queue is the right structure for this scenario,")
    print("since it preserves fairness by serving people in arrival order —")
    print("something a Stack (LIFO) could not do.")
    print("\n=== END OF REAL-WORLD SCENARIO ===\n")
 
 
if __name__ == "__main__":
    main()