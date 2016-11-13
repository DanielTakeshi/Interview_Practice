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


def question_01_test():
    """ Question 1 practice. Things look good! """
    print("Question 1 stuff!")
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
    print("")


def question_02(slist, k):
    """ Optional challenge: using slist._size is not allowed.  Looking for k-th
    last, so k=1 means last, k=2 means penultimate, etc.  Returns None if the
    list is not as large as k. if k <= 0, exception.
    """
    # Handle cases of invalid k and list of length 0
    if k <= 0:
        raise ValueError("k = {}, not valid".format(k))
    if slist._head == None:
        return None

    current = slist._head
    runner = slist._head
    i = 1
    while runner._next != None and i < k:
        runner = runner._next
        i += 1

    # Case of when there aren't enough elements in list for k-th last to exist.
    if i < k:
        return None

    while runner._next != None:
        runner = runner._next
        current = current._next
    return current._item


def question_02_test():
    """ Question 2 testing. Looks good! =). """
    print("Question 2 stuff!")
    x = SList()
    question_02(x,1)
    print(x.to_string())
    x.insert_front("a")
    print(x.to_string())
    print("1st-last: {}".format(question_02(x,1)))
    print("2st-last: {}".format(question_02(x,2)))

    x.insert_front("b")
    print(x.to_string())
    print("1st-last: {}".format(question_02(x,1)))
    print("2st-last: {}".format(question_02(x,2)))
    print("3rd-last: {}".format(question_02(x,3)))

    x.insert_front("c")
    print(x.to_string())
    print("1st-last: {}".format(question_02(x,1)))
    print("2st-last: {}".format(question_02(x,2)))
    print("3rd-last: {}".format(question_02(x,3)))
    print("4th-last: {}".format(question_02(x,4)))

    x.insert_front("d")
    print(x.to_string())
    print("1st-last: {}".format(question_02(x,1)))
    print("2st-last: {}".format(question_02(x,2)))
    print("3rd-last: {}".format(question_02(x,3)))
    print("4th-last: {}".format(question_02(x,4)))
    print("5th-last: {}".format(question_02(x,5)))

    x.insert_front("d")
    print(x.to_string())
    print("1st-last: {}".format(question_02(x,1)))
    print("2st-last: {}".format(question_02(x,2)))
    print("3rd-last: {}".format(question_02(x,3)))
    print("4th-last: {}".format(question_02(x,4)))
    print("5th-last: {}".format(question_02(x,5)))
    print("6th-last: {}".format(question_02(x,6)))

    print("")


def question_03(slist, node_del):
    if slist._head == None:
        return

    # Special case, start of list.
    if slist._head == node_del:
        slist._head = slist._head._next
        return
    current = slist._head

    # More general case, arbitrary location after first one.
    while (current._next != None):
        if current._next == node_del:
            current._next = current._next._next
            return # node_del can only refer to one thing (I hope)
        else:
            current = current._next


def question_03_test():
    """ I think it works ... BUT the question was a bit of a trick. """
    print("Question 3 stuff!")
    x = SList()
    x.insert_front("x")
    x.insert_front("y")
    x.insert_front("z")
    s = x._head._next._next # keep switching this
    print(x.to_string())
    question_03(x, s)
    print(x.to_string())
    print("")


def question_04(slist, x):
    """ Partitions values about some (integer) value.
    slist = the linked list (header)
    x = the value about which to partition.
    """
    if slist._size <= 1:
        return
    p = slist._head

    while p._next != None:
        if p._next._item < x:
            copy = p._next # Store copy of the (next) SListNode
            p._next = p._next._next
            copy._next = slist._head
            slist._head = copy
        else:
            p = p._next


def question_04_test():
    """ """
    print("Question 4 stuff!")

    x = SList()
    x.insert_front(10)
    x.insert_front(7)
    print("Doesn't need re-ordering")
    print(x.to_string())
    question_04(x, 10)
    print(x.to_string())

    y = SList()
    y.insert_front(7)
    y.insert_front(10)
    print("Needs re-ordering")
    print(y.to_string())
    question_04(y, 10)
    print(y.to_string())

    z = SList()
    z.insert_front(11)
    z.insert_front(7)
    z.insert_front(10)
    z.insert_front(15)
    z.insert_front(1)
    z.insert_front(10)
    z.insert_front(16)
    z.insert_front(9)
    print("Needs re-ordering")
    print(z.to_string())
    question_04(z, 10)
    print(z.to_string())
    print("")


def question_05():
    pass


def question_05_test():
    print("Question 5 stuff!")
    print("")


def question_06():
    pass


def question_06_test():
    print("Question 6 stuff!")
    print("")


def question_07(dlist):
    """ For simplicity, let's assume it's **doubly linked**, if it were singly
    linked, it's the same except we need a pointer to go to the end. """

    # Some special cases out of the way.
    if dlist._size <= 1:
        return True

    left = dlist._sentinel._next
    right = dlist._sentinel._prev

    # Assume we know the size (if it's odd, it rounds down, which is OK).
    for _ in range(dlist._size / 2):
        if (left._item != right._item):
            return False
        left = left._next
        right = right._prev
    return True


def question_07_test():
    print("Question 7 stuff!")
    d = DList()
    d.insert_front("a")
    print(d.to_string())
    print(question_07(d))
    d.insert_front("a")
    print(d.to_string())
    print(question_07(d))
    d.insert_front("a")
    print(d.to_string())
    print(question_07(d))
    d.insert_front("b")
    print(d.to_string())
    print(question_07(d))
    
    d = DList()
    d.insert_front("s")
    d.insert_front("o")
    d.insert_front("r")
    d.insert_front("r")
    d.insert_front("o")
    d.insert_front("s")
    print(d.to_string())
    print(question_07(d))
    print("")


if __name__ == "__main__":
    # Quetion 1 stuff
    question_01_test()

    # Question 2 stuff
    question_02_test()

    # Question 3 stuff
    question_03_test()

    # Question 4 stuff
    question_04_test()

    # Question 5 stuff
    question_05_test()

    # Question 6 stuff
    question_06_test()

    # Question 7 stuff
    question_07_test()
