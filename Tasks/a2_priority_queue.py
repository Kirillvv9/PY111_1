"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any


class PriorityQueue:
    def __init__(self):
        self.priority_queue = {}

    def enqueue(self, elem: Any, priority: int = 0) -> None:
        """
        Operation that add element to the end of the queue

        :param elem: element to be added
        :return: Nothing
        """
        self.priority_queue[priority] = self.priority_queue.get(priority, [])
        self.priority_queue[priority].append(elem)
        return None

    def dequeue(self) -> Any:
        """
        Return element from the beginning of the queue. Should return None if not elements.

        :return: dequeued element
        """
        if self.priority_queue:
            del_elem = self.priority_queue[min(self.priority_queue)][0]
            del self.priority_queue[min(self.priority_queue)][0]
            if len(self.priority_queue[min(self.priority_queue)]) == 0:
                del self.priority_queue[min(self.priority_queue)]
                return del_elem
        else:
            return None

    def peek(self, ind: int = 0, priority: int = 0) -> Any:
        """
        Allow you to see at the element in the queue without dequeuing it

        :param ind: index of element (count from the beginning)
        :return: peeked element
        """
        peek_value = self.priority_queue[priority][ind]
        if peek_value is not None:
            return peek_value
        else:
            return None

    def clear(self) -> None:
        """
        Clear my queue

        :return: None
        """
        self.priority_queue.clear()
        return None
