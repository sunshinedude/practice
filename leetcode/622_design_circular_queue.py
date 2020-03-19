# Problem

# Design your implementation of the circular queue.
# The circular queue is a linear data structure in which the operations are performed based on
# FIFO (First In First Out) principle and the last position is connected back to the first position
# to make a circle. It is also called "Ring Buffer".
#
# One of the benefits of the circular queue is that we can make use of the spaces in
# front of the queue. In a normal queue, once the queue becomes full,
# we cannot insert the next element even if there is a space in front of the queue.
# But using the circular queue, we can use the space to store new values.
#
# Your implementation should support following operations:
#
# MyCircularQueue(k): Constructor, set the size of the queue to be k.
# Front: Get the front item from the queue. If the queue is empty, return -1.
# Rear: Get the last item from the queue. If the queue is empty, return -1.
# enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
# deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
# isEmpty(): Checks whether the circular queue is empty or not.
# isFull(): Checks whether the circular queue is full or not.

# Solution


class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        """
        self.max_size = k
        self.current_size = 0
        self.head = 0
        self.tail = -1
        self.q = [0 for _ in range(k)]

    def enQueue(self, value: int) -> bool:
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        """
        if self.isFull():
            return False
        self.current_size += 1
        if self.tail < self.max_size -1:
            self.tail += 1
        else:
            self.tail = 0
        self.q[self.tail] = value
        return True

    def deQueue(self) -> bool:
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        """
        if self.isEmpty():
            return False

        self.current_size -= 1

        if self.isEmpty():
            self.head = 0
            self.tail = -1
            return True

        if self.head < self.max_size - 1:
            self.head += 1
        else:
            self.head = 0
        return True

    def Front(self) -> int:
        """
        Get the front item from the queue.
        """
        return -1 if self.isEmpty() else self.q[self.head]

    def Rear(self) -> int:
        """
        Get the last item from the queue.
        """
        return -1 if self.isEmpty() else self.q[self.tail]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return not bool(self.current_size)

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.max_size == self.current_size
