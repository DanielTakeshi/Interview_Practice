""" 
My attempt at answering question 1 with a flexible array.
(c) 2017
"""

class ThreeStacksOneArray:

    def __init__(self):
        self.s = [3,4,5]

    def push(self, item, stack_index):
        assert stack_index in [0,1,2]
        next_free_index = self._get_next_free_index(stack_index)
        if len(self.s) <= next_free_index:
            self._resize(double=True)
        self.s[next_free_index] = item
        self.s[stack_index] += 3

    def pop(self, stack_index):
        assert stack_index in [0,1,2]
        top_index = self._get_next_free_index(stack_index) - 3
        if top_index <= 2:
            return None # Empty stack
                            
        self.s[top_index] = None
        self.s[stack_index] -= 3
        n = len(self.s)
        if self.s[0]<n/2 and self.s[1]<n/2 and self.s[2]<n/2:
            self._resize(double=False)

    def _get_next_free_index(self, stack_index):
        return self.s[stack_index]

    def _resize(self, double=True):
        """ Either double or halve the list for space reasons. """
        n = len(self.s)
        if double:
            for _ in range(n):
                self.s.append(None)
        else:
            self.s = self.s[:int(n/2)]

    def __str__(self):
        return self.s.__str__()

if __name__ == "__main__":
    s = ThreeStacksOneArray()
    print(s)
    print("See what happens when we pop empty stack:")
    s.pop(0)
    print(s)
    s.pop(1)
    print(s)
    s.pop(2)
    print(s)
    print("Now let's push.")
    s.push(100,2)
    print(s)
    s.push(200,2)
    print(s)
    s.push(300,2)
    print(s)
    s.push(400,2)
    print(s)
    s.push(-10,1)
    print(s)
    s.push(0,0)
    print(s)
    print("now pop ...")
    s.pop(2)
    print(s)
    s.pop(1)
    print(s)
    s.pop(2)
    print(s)
    s.pop(2)
    print(s)
    s.pop(2)
    print(s)
    s.pop(2)
    print(s)
