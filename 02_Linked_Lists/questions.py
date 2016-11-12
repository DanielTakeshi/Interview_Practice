"""
Linked list questions
"""

from hash_table import *

def question_01(slist):
    """ Assumes 'slist' is of type SList. Removes duplicates but no buffer
    allowed. """

    if slist._size <= 1:
        return
    s1 = slist._head
    s2 = slist._head

    while (s1 != None):
        while (s2._next != None):
            if (s1._item == s2._next._item):
                s2._next = s2._next._next
            else:
                s2 = s2._next
        s1 = s1._next
        s2 = s1

if __name__ == "__main__":
    x = SList()
    question_01(x)
    print(x.to_string())

    x.insert_front("fish")
    question_01(x)
    print(x.to_string())

    x.insert_front("fish")
    print(x.to_string())
    question_01(x)
    print(x.to_string())

    y = SList()
    y.insert_front("hi")
    y.insert_front("hi")
    y.insert_front("bye")
    y.insert_front("no")
    y.insert_front("hi")
    y.insert_front("bye")
    y.insert_front("what")
    y.insert_front("hi")
    print(y.to_string())
    question_01(y)
    print(y.to_string())
