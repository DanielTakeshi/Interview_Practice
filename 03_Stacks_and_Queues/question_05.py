""" 
My attempt at answering question 5. We'll use two Stacks to make a queue.
(c) 2017
"""

from stack_queue import Stack

class MyQueue:

    def __init__(self):
        self.s1 = Stack() # Use for dequeues
        self.s2 = Stack() # Use for reverse ordering

    def enqueue(self, item):
        #while not self.s1.is_empty():
        while self.s1.peek() is not None:
            self.s2.push( self.s1.pop() )
        self.s2.push(item)
        #while not self.s2.is_empty():
        while self.s2.peek() is not None:
            self.s1.push( self.s2.pop() )

    def dequeue(self):
        return self.s1.pop()

    def __str__(self):
        return "s1: {}\ns2: {}".format(self.s1.__str__(), 
                                       self.s2.__str__())
    
if __name__ == "__main__":
    q = MyQueue()
    print("\n{}".format(q))

    for i in range(1,7):
        q.enqueue(i)
        print("\n{}".format(q))

    for _ in range(3):
        q.dequeue()
        print("\n{}".format(q))

    for i in range(7,9):
        q.enqueue(i)
        print("\n{}".format(q))
