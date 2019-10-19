class Stack:
    """Top here means the end of the list.

    Stacks are often well suited with some recursive problems, or those with a
    symmetric, such as of parentheses matching.
    """

    def __init__(self):
        """Add/remove in O(1) time, but not constant-time access to i-th item."""
        self.s = []

    def __str__(self):
        s = 'S: [bot]  {}  [top]'.format(self.s)
        return s

    def pop(self):
        """Remove top item from the stack."""
        assert len(self.s) >= 1
        self.s = self.s[:-1]

    def push(self, item):
        """Add an item to the top of the stack."""
        self.s.append(item)

    def peek(self):
        """Return the top item of the stack (w/o removing it)."""
        assert len(self.s) >= 1
        return self.s[-1]

    def is_empty(self):
        """Return true if and only if the stack is empty."""
        return len(self.s) == 0


class Queue:
    """Top here means the beginning of the list.

    Queues can be useful for breadth-first search.
    """

    def __init__(self):
        """Add/remove in O(1) time, but not constant-time access to i-th item.

        I think --- might actually have to be careful with memory but I think
        this is true in theory. A linked list might be a better match.
        """
        self.q = []

    def __str__(self):
        q = 'Q: [top]  {}  [bot]'.format(self.q)
        return q

    def add(self, item):
        """Add an item to the end of the list."""
        self.q.append(item)

    def remove(self):
        """Remove the first item in the list."""
        assert len(self.q) >= 1
        self.q = self.q[1:]

    def peek(self):
        """Return the top of the queue (w/o removing it)."""
        assert len(self.q) >= 1
        return self.q[0]

    def is_empty(self):
        """Return true if and only if the queue is empty."""
        return len(self.q) == 0


def stack01():
    s = Stack()
    s.push(1)
    s.push(3)
    s.push(5)
    s.push(7)
    return s


def stack02():
    s = Stack()
    s.push(1)
    s.push(3)
    s.pop()
    s.push(7)
    return s


def stack03():
    s = Stack()
    s.push(1)
    s.push(3)
    s.pop()
    s.push(7)
    s.pop()
    s.push(1)
    return s


def stack04():
    s = Stack()
    s.push(1)
    s.push(3)
    s.push(5)
    s.push(7)
    s.pop()
    s.pop()
    s.pop()
    return s


def queue01():
    q = Queue()
    q.add(2)
    q.add(4)
    q.add(6)
    q.add(8)
    return q


def queue02():
    q = Queue()
    q.add(2)
    q.add(4)
    q.remove()
    q.add(8)
    return q


def queue03():
    q = Queue()
    q.add(2)
    q.add(4)
    q.add(6)
    q.add(8)
    q.remove()
    q.remove()
    q.add(9)
    return q


def queue04():
    q = Queue()
    q.add(2)
    q.add(4)
    q.add(6)
    q.add(8)
    q.remove()
    q.remove()
    q.remove()
    q.remove()
    return q


## ------------------------ PROBLEM 01 ------------------------ ##

## ------------------------ PROBLEM 02 ------------------------ ##

class StackMin:

    def __init__(self):
        self.s = []

    def push(self, item):
        """Instead of a normal stack, add min item in tuple."""
        if len(self.s) == 0:
            min_v = item
        else:
            min_v = min(self.min(), item)
        stack_item = (item, min_v)
        self.s.append( stack_item )

    def pop(self):
        """Remove item, assume we need >1 items."""
        assert len(self.s) >= 1
        self.s = self.s[:-1]

    def min(self):
        """Return minimum item, assume >1 items."""
        assert len(self.s) >= 1
        item, min_item = self.s[-1]
        return min_item

    def __str__(self):
        s = '[bot]  {}  [top]'.format(self.s)
        return s

## ------------------------ PROBLEM 03 ------------------------ ##

## ------------------------ PROBLEM 04 ------------------------ ##

## ------------------------ PROBLEM 05 ------------------------ ##

## ------------------------ PROBLEM 06 ------------------------ ##

## ------------------------ PROBLEM 07 ------------------------ ##



if __name__ == "__main__":
    # ----------------- Debug stacks/queues ----------------
    stacks = [stack01(), stack02(), stack03(), stack04()]
    for s in stacks:
        print(s)
    print()
    queues = [queue01(), queue02(), queue03(), queue04()]
    for q in queues:
        print(q)

    # ----------------- Problem 02 ----------------
    print('')
    print('-'*120)
    print('PROBLEM 2\n')
    sm = StackMin()
    sm.push(3)
    print('Stack w/min item {}: {}\n'.format(sm.min(), sm))
    sm.push(4)
    print('Stack w/min item {}: {}\n'.format(sm.min(), sm))
    sm.push(1)
    print('Stack w/min item {}: {}\n'.format(sm.min(), sm))
    sm.pop()
    print('Stack w/min item {}: {}\n'.format(sm.min(), sm))
    sm.push(-4)
    print('Stack w/min item {}: {}\n'.format(sm.min(), sm))
    sm.push(1)
    print('Stack w/min item {}: {}\n'.format(sm.min(), sm))
    sm.push(-10)
    print('Stack w/min item {}: {}\n'.format(sm.min(), sm))
    sm.pop()
    print('Stack w/min item {}: {}\n'.format(sm.min(), sm))
    sm.pop()
    print('Stack w/min item {}: {}\n'.format(sm.min(), sm))
