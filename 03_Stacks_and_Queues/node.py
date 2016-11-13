"""
Test implementation of Hash Tables which use linked lists (avoids problems with
arrays of adding/removing which requires shifting elements, and also
re-allocating memory if array is full). Try to minimize external libraries, i.e.
use plain Python.
"""
import sys

class SListNode:
    """ Singly-linked Node, references to any object. """

    def __init__(self, i, n=None):
        self._item = i
        self._next = n


class SList:
    """ A class whose job is to maintain the first node of an SListNode.
    Enforces the invariants that the size is always correct, and the list is
    never circularly linked.
    """

    def __init__(self, h=None):
        self._head = h
        self._size = 0

    def insert_front(self, item):
        self._head = SListNode(item, self._head)
        self._size += 1

    def to_string(self):
        if self._size == 0:
            return "[head] -> [None]"
        l_str = "[head] -> " + str(self._head._item)
        node = self._head
        while node._next != None:
            node = node._next
            l_str += " -> " + str(node._item)
        return l_str + " -> [None]"


class DListNode:
    """ Doubly-linked Node, references to any object. """

    def __init__(self, i, n=None, p=None):
        self._item = i
        self._next = n
        self._prev = p


class DList:
    """ Similar to SList, except for the doubly-linked version. This points to
    the `sentinel` which does not represent an item. To detect if we are at the
    Sentinel, check that the item is equal to SENTINEL (a special item that we
    assume we never have in our real items). """

    def __init__(self):
        self._sentinel = DListNode("SENTINEL", n=None, p=None)
        self._sentinel._next = self._sentinel
        self._sentinel._prev = self._sentinel
        self._size = 0

    def insert_front(self, item):
        if self._size == 0:
            d = DListNode(item, n=self._sentinel, p=self._sentinel)
            self._sentinel._next = d
            self._sentinel._prev = d
        else:
            d = DListNode(item, n=self._sentinel._next, p=self._sentinel)
            self._sentinel._next._prev = d
            self._sentinel._next = d
        self._size += 1

    def remove_last(self):
        if (self._sentinel._prev != self._sentinel):
            # The below is correct, but simpler to do it other way around.
            #self._sentinel._prev._prev._next = self._sentinel
            #self._sentinel._prev = self._sentinel._prev._prev
            # Reversed (though one statement is exactly the same):
            self._sentinel._prev = self._sentinel._prev._prev
            self._sentinel._prev._next = self._sentinel
            self._size -= 1

    def to_string(self):
        if self._size == 0:
            return "[head] -> [sentinel]"
        node = self._sentinel._next
        l_str = "[head] -> [sentinel] -> " + str(node._item)
        while node._next._item != "SENTINEL":
            node = node._next
            l_str += " -> " + str(node._item)
        return l_str + " -> [sentinel]"


# Now let's practice and test things out!
if __name__ == "__main__":

    # SLists
    print("Debugging with SLists:")
    x = SList()
    y = SList()
    y.insert_front("blue")
    y.insert_front("rasp")

    print(x.to_string())
    x.insert_front("milk")
    print(x.to_string())
    x.insert_front("fish")
    print(x.to_string())
    print(y.to_string())

    # DLists
    print("\nNow on DLists:")
    d = DList()
    print(d.to_string())
    d.insert_front("obama")
    print(d.to_string())
    d.insert_front("bush43")
    print(d.to_string())
    d.insert_front("clinton")
    print(d.to_string())
    d.insert_front("bush41")
    print(d.to_string())
    d.remove_last()
    print(d.to_string())
    d.remove_last()
    print(d.to_string())
    d.remove_last()
    print(d.to_string())
    d.remove_last()
    print(d.to_string())
    d.remove_last()
    print(d.to_string())
    d.insert_front("obama")
    print(d.to_string())
