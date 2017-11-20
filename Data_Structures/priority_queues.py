""" Practice w/PQs and Heaps. """

class Entry:
    """ The components within priority queues. """
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        res = "[{} --> {}]".format(self.key, self.value)
        return res

import numpy as np

class PriorityQueue:

    def __init__(self):
        # Add `None` at the start to make the indexing work out.  Thus, the
        # minimum would be at index 1, not 0. And thus self.size =
        # len(self.entries)-1. From JRS: Observe that if a node’s index is i,
        # its children’s indices are 2i and 2i+1, and its parent’s index is
        # floor(i/2).
        self.entries = [None]
        self.size = 0

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert(self, key, value):
        """ Insert at the end, then bubble up. """
        node_to_add = Entry(key, value)
        self.entries.append(node_to_add)
        idx = len(self.entries)-1

        while idx > 1:
            idx_parent = int(idx/2)
            parent = self.entries[idx_parent]
            if key < parent.key:
                self.entries[idx] = parent
                self.entries[idx_parent] = node_to_add
                idx = idx_parent
            else:
                break
        self.size += 1

    def min(self):
        if self.is_empty():
            raise ValueError("PQ is empty.")
        return self.entries[1]

    def remove_min(self):
        if self.is_empty():
            raise ValueError("PQ is empty.")
        entry = self.entries[1]

        # Bring the last index to front.
        last = self.entries[-1]
        self.entries = self.entries[:-1]
        self.entries[1] = last
        idx = 1
        idx_left = 2*idx
        idx_right = 2*idx + 1

        # If condition equivalent to testing if we're at a leaf.
        while idx_left < len(self.entries):
            # We know there is a left key. But test for right.
            key_l = self.entries[idx_left].key
            if idx_right < len(self.entries):
                key_r = self.entries[idx_right].key
            else:
                key_r = np.float('inf')

            # Now test for comparisions. If we don't break,
            # we know we have to swap.
            tmp = self.entries[idx]
            if key_l < key_r:
                if self.entries[idx].key <= key_l:
                    break
                self.entries[idx] = self.entries[idx_left]
                self.entries[idx_left] = tmp
                idx = idx_left
            else:
                if self.entries[idx].key <= key_r:
                    break
                self.entries[idx] = self.entries[idx_right]
                self.entries[idx_right] = tmp
                idx = idx_right

            # Update indices here.
            idx_left = 2*idx
            idx_right = 2*idx + 1

        self.size -= 1
        return entry

    def __str__(self):
        s = "["
        for e in self.entries[1:]:
            s += " ({},{}),".format(e.key,e.value)
        s += " ]"
        return s


if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq)
    pq.insert(4,"oakland")
    print(pq)
    pq.insert(1,"berkeley")
    print(pq)
    pq.insert(3,"cupertino")
    print(pq)
    pq.insert(10,"monterey bay")
    print(pq)
    pq.insert(12,"san francisco")
    pq.insert(2,"sacramento")
    pq.insert(11,"los angeles")
    pq.insert(8,"irvine")
    pq.insert(8,"irvinev2")
    pq.insert(7,"san diego")
    pq.insert(15,"malibu")
    print(pq)

    print("\nnow let's test removing ...")
    e = pq.remove_min()
    print(pq)
    e = pq.remove_min()
    print(pq)
    e = pq.remove_min()
    print(pq)   
    e = pq.remove_min()
    print(pq)
