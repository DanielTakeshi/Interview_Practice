"""
Questions for stacks and queues.
Skipping question 1 for now; it's too long.
"""

from node import SListNode
from stack_queue import Stack

class StackMin:
    """ Contains min functionality by using (item, current_min) instead of
    (item).  The top of the stack is the first list node (the one most recently
    added).  """

    def __init__(self):
        self.top = None

    def pop(self):
        if (self.top != None):
            datum = self.top._item[0]
            self.top = self.top._next
            return datum
        return None

    def push(self, item):
        current_min = self.min_element()
        if (current_min == None or item < current_min):
            current_min = item
        node = SListNode((item,current_min), self.top)
        self.top = node

    def min_element(self):
        if (self.top != None):
            return self.top._item[1]
        return None

    def to_string(self):
        result = "[top]"
        k = self.top
        while (k != None):
            result += " -- " + str(k._item)
            k = k._next
        return result + " -- [bottom]"


def question_02_test():
    """ Yes, I think this works!! """
    print("Question 2 stuff!")
    s = StackMin()
    print(s.to_string())
    s.push(25)
    print(s.to_string())
    s.push(35)
    print(s.to_string())
    s.push(21)
    print(s.to_string())
    s.push(34)
    print(s.to_string())
    s.push(17)
    print(s.to_string())
    s.push(5)
    print(s.to_string())
    s.push(9)
    print(s.to_string())
    print(s.min_element())
    s.pop()
    s.pop()
    s.pop()
    print(s.to_string())
    print(s.min_element())
    print("")


class MyQueue:
    """ For Question 5. """

    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def enqueue(self, item):
        """ Add to end. """
        self.s1.push(item)

    def dequeue(self):
        """ Remove from front. """
        if self.s1.is_empty():
            return None
        while (not self.s1.is_empty()):
            self.s2.push( self.s1.pop() )
        result = self.s2.pop()
        while (not self.s2.is_empty()):
            self.s1.push( self.s2.pop() )       
        return result


def question_05_test():
    """ Using Stack, not StackMin, but shouldn't matter. I think it's OK. """
    print("Question 5 stuff!")
    q = MyQueue()
    q.enqueue("a")
    q.enqueue("b")
    q.enqueue("c")
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print("")


if __name__ == "__main__":
    # Question 2 tests
    question_02_test()

    # Question 5 tests
    question_05_test()
