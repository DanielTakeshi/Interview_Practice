"""
In 2017, trying question 3
"""

from stack_queue import Stack

class SetOfStacks:

    def __init__(self, capacity):
        self.stacks = []
        self.sizes = []
        assert capacity > 0
        self.capacity = capacity

    def push(self, item):
        # Keep stacks and sizes lists of the same length
        if len(self.sizes)==0 or self.sizes[-1]==self.capacity:
            self.stacks.append(Stack())
            self.sizes.append(1)
        else:
            self.sizes[-1] += 1
        (self.stacks[-1]).push(item)

    def pop(self):
        # Handle completely empty case first.
        if len(self.sizes) == 0:
            return None
                                            
        # otherwise there exists _something_ in our lists.
        # if we removed the only item, we get rid of the stack.
        # we assume that we have at least one thing in the last
        item = (self.stacks[-1]).pop()
        self.sizes[-1] -= 1

        if self.sizes[-1] == 0:
            self.stacks = self.stacks[:-1]
            self.sizes = self.sizes[:-1]
        return item

    def __str__(self):
        result = "\n"
        for i in range(len(self.stacks)):
            result += "{}, {}:  {}\n".format(i, self.sizes[i], self.stacks[i])
        return result

if __name__ == "__main__":
    s = SetOfStacks(capacity=1)
    print(s)
    s.pop()
    print(s)

    for i in range(10):
        s.push(i)
        print(s)

    for _ in range(4):
        s.pop()
        print(s)

    for i in range(10,12):
        s.push(i)
        print(s)
