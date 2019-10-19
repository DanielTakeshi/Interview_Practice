"""
Stacks and Queues.
"""

class SListNode:
    def __init__(self, i=None, n=None):
        self._item = i
        self._next = n


class Stack:
    """ Linked-list based Stack implementation. The top of the stack here refers
    to the first linked list (think of insert front as inserting at the top).
    For now also assume that this contains numbers only (so items are not
    strings), because one of the problems asks to design a stack which returns
    the minimum element. Anything with a partial ordering would work, though...
    """

    def __init__(self, top=None):
        self.top = top

    def pop(self):
        """ Returns the item on the top (NOT an SListNode, but it's ITEM). """
        if (self.top != None):
            datum = self.top._item
            self.top = self.top._next
            return datum
        return None

    def push(self, item):
        """ Push an item on the stack (NOT an SListNode, JUST it's ITEM). """
        t = SListNode(i=item, n=self.top)
        self.top = t

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.top._item

    def to_string(self):
        result = "[top]"
        k = self.top
        while (k != None):
            result += " -- " + str(k._item)
            k = k._next
        return result + " -- [bottom]"

    def __str__(self):
        return self.to_string()

    def is_empty(self):
        """ A useful helper/convenience method. """
        return (self.top == None)


class Queue:
    """ Linked-list based Queue implementation. The "last" here refers to the
    spot that elements go FIRST in the queue (so they are LAST to get out). A
    bit confusing to wrap around ... """

    def __init__(self, first=None, last=None):
        self.first = first # Refers to the first one OUT
        self.last = last

    def enqueue(self, item):
        if (self.first == None):
            self.last = SListNode(i=item, n=None)
            self.first = self.last
        else:
            self.last._next = SListNode(i=item, n=None)
            self.last = self.last._next

    def dequeue(self):
        if (self.first != None):
            datum = self.first._item
            self.first = self.first._next
            if (self.first == None):
                self.last = self.first
            return datum
        return None

    def to_string(self):
        result = "[first_in_line]"
        k = self.first
        while (k != None):
            result += " -- " + str(k._item)
            k = k._next
        return result + " -- [last_in_line]"

if __name__ == "__main__":
    print("stacks:")
    s = Stack()
    print("isempty:" + str(s.is_empty()))
    print(s.to_string())
    s.push("washington")
    s.push("jadams")
    s.push("jefferson")
    print(s.to_string())
    print("peek: " + str(s.peek()))
    s.pop()
    print("isempty:" + str(s.is_empty()))
    print(s.to_string())
    s.pop()
    print(s.to_string())
    s.pop()
    print(s.to_string())
    s.pop()
    print(s.to_string())
    print("isempty:" + str(s.is_empty()))

    print("\nqueues:")
    q = Queue()
    print(q.to_string())
    q.enqueue("no")
    print(q.to_string())
    q.enqueue("yes")
    print(q.to_string())
    q.enqueue("!!")
    print(q.to_string())
    q.enqueue("creep")
    print(q.to_string())
    q.dequeue()
    print(q.to_string())
    q.dequeue()
    print(q.to_string())
    q.dequeue()
    print(q.to_string())
