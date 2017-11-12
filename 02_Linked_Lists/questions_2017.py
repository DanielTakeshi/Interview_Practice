""" Linked list questions. 2017 Edition. """

from linked_lists import *
import sys

def question_01(slist):
    current = slist._head

    while current is not None:
        item = current._item
        runner = current
        while runner._next is not None:
            if runner._next._item == item:
                runner._next = runner._next._next
            else:
                runner = runner._next
        current = current._next


def question_01_bad(slist):
    """ Fails on [x] -> [x] input. """
    current = slist._head
    if current is None:
        return

    while current._next is not None:
        item = current._item
        runner = current
        while runner._next is not None:
            if runner._next._item == item:
                runner._next = runner._next._next
            else:
                runner = runner._next
        current = current._next


def question_01_test():
    """ Question 1 practice. Things look good! """
    print("\n\nQuestion 1 stuff!")
    x = SList()
    print("our list:\n{}".format(x))
    question_01(x)
    print("after applying q01:\n{}".format(x))

    x.insert_front("fish")
    print("our list:\n{}".format(x))
    question_01(x)
    print("after applying q01:\n{}".format(x))

    x.insert_front("fish")
    print("our list:\n{}".format(x))
    question_01(x)
    print("after applying q01:\n{}".format(x))

    print("\nnow we're starting a new list ...")
    y = SList()
    y.insert_front("hi")
    y.insert_front("hi")
    y.insert_front("bye")
    y.insert_front("no")
    y.insert_front("hi")
    y.insert_front("bye")
    y.insert_front("what")
    y.insert_front("hi")
    print(y)
    question_01(y)
    print("after applying q01:\n{}".format(y))


def question_02(slist, k):
    """ 
    Optional challenge: using slist._size is not allowed.  Looking for k-th
    last, so k=1 means last, k=2 means penultimate, etc.  Returns None if the
    list is not as large as k. if k <= 0, error.
    """
    assert k >= 1
    if slist._head is None:
        return None
    current = slist._head
    runner = current

    # Get the runner k spots ahead (k-1 actually makes the indexing work)
    for i in range(k-1):
        if runner._next is not None:
            runner = runner._next
        else:
            return None

    # Move them both now
    while runner._next is not None:
        runner = runner._next
        current = current._next
    return current._item


def question_02_test():
    """ Question 2 testing. Looks good! =). """
    print("\n\nQuestion 2 stuff!")
    x = SList()
    question_02(x,1)
    print(x)
    x.insert_front("a")
    print(x)
    print("1st-last: {}".format(question_02(x,1)))
    print("2st-last: {}".format(question_02(x,2)))

    x.insert_front("b")
    print(x)
    print("1st-last: {}".format(question_02(x,1)))
    print("2st-last: {}".format(question_02(x,2)))
    print("3rd-last: {}".format(question_02(x,3)))

    x.insert_front("c")
    print(x)
    print("1st-last: {}".format(question_02(x,1)))
    print("2st-last: {}".format(question_02(x,2)))
    print("3rd-last: {}".format(question_02(x,3)))
    print("4th-last: {}".format(question_02(x,4)))

    x.insert_front("d")
    print(x)
    print("1st-last: {}".format(question_02(x,1)))
    print("2st-last: {}".format(question_02(x,2)))
    print("3rd-last: {}".format(question_02(x,3)))
    print("4th-last: {}".format(question_02(x,4)))
    print("5th-last: {}".format(question_02(x,5)))

    x.insert_front("d")
    print(x)
    print("1st-last: {}".format(question_02(x,1)))
    print("2st-last: {}".format(question_02(x,2)))
    print("3rd-last: {}".format(question_02(x,3)))
    print("4th-last: {}".format(question_02(x,4)))
    print("5th-last: {}".format(question_02(x,5)))
    print("6th-last: {}".format(question_02(x,6)))


def question_03(node_del):
    """ 
    Here, node_del is an SListNode to delete ...  will not work if the node is
    the last one. Which is fine. Gah. 
    """
    assert node_del is not None
    assert node_del._next is not None
    node_del._item = node_del._next._item
    node_del._next = node_del._next._next

def question_03_test():
    """ I think it works ... """
    print("\n\nQuestion 3 stuff!")
    x = SList()
    x.insert_front("x")
    x.insert_front("y")
    x.insert_front("z")
    # Works for removing y and z. :-)
    s = x._head._next 
    print(x)
    print("going to remove item: {}".format(s._item))
    question_03(s)
    print(x)


def question_04(slist, x):
    """  
    Should be OK, but I think Gayle has a cleaner, easier to understand solution
    which is equivalent in terms of memory and running costs.
    """
    current = slist._head
    if current is None or current._next is None:
        return
    while current._next is not None:
        if current._next._item < x:
            # Move current._next to the front, change three references
            next_copy = current._next # O.w. current._next could be None
            current._next = current._next._next 
            next_copy._next = slist._head
            slist._head = next_copy
        else:
            current = current._next

def question_04_test():
    print("\n\nQuestion 4 stuff!")

    x = SList()
    x.insert_front(10)
    x.insert_front(7)
    print("Doesn't need re-ordering for thresh 10")
    print(x)
    question_04(x, 10)
    print(x)

    y = SList()
    y.insert_front(7)
    y.insert_front(10)
    print("Needs re-ordering for thresh 10")
    print(y)
    question_04(y, 10)
    print(y)

    z = SList()
    z.insert_front(11)
    z.insert_front(7)
    z.insert_front(10)
    z.insert_front(15)
    z.insert_front(1)
    z.insert_front(10)
    z.insert_front(16)
    z.insert_front(9)
    print("Needs re-ordering for thresh 10")
    print(z)
    question_04(z, 10)
    print(z)


def question_05(xlist, ylist):
    """ I think this works. :-) """
    xcurrent = xlist._head
    ycurrent = ylist._head
    assert xcurrent is not None and ycurrent is not None

    def get_digit_and_carry(value):
        digit = value % 10
        carry = int(value / 10)
        return digit, carry

    # Put digits here, least significant to most.  Make l-list later.
    sum_digits = [] 
    carry = 0

    while xcurrent is not None and ycurrent is not None:
        assert 0 <= xcurrent._item <= 9
        assert 0 <= ycurrent._item <= 9
        digit, carry = get_digit_and_carry( xcurrent._item+ycurrent._item+carry )
        sum_digits.append(digit)
        xcurrent = xcurrent._next
        ycurrent = ycurrent._next

    # But now one of the lists could have remaining stuff. Find it.
    remainder = None
    if xcurrent is not None:
        remainder = xcurrent
    elif ycurrent is not None:
        remainder = ycurrent

    # Then sum up the stuff. Skip entirely if both were None.
    while remainder is not None:
        assert 0 <= remainder._item <= 9
        digit, carry = get_digit_and_carry( remainder._item + carry ) 
        sum_digits.append(digit)
        remainder = remainder._next    

    # Don't forget about that carry!
    while carry != 0:
        sum_digits.append( carry % 10 )
        carry = int(carry / 10)

    # Finally, form the list from sum_digits.
    sum_list = SList()
    for digit in sum_digits[::-1]:
        sum_list.insert_front(digit)
    return sum_list


def question_05_test():
    print("\n\nQuestion 5 stuff!")
    x = SList()
    x.insert_front(1)
    y = SList()
    y.insert_front(3)
    y.insert_front(4)
    print("The two lists (1+34 = 35):")
    print("  x: {}".format(x))
    print("  y: {}".format(y))
    print(question_05(x, y))

    x = SList()
    x.insert_front(6)
    x.insert_front(1)
    x.insert_front(7)
    y = SList()
    y.insert_front(2)
    y.insert_front(9)
    y.insert_front(5)
    print("The two lists (617+295 = 912):")
    print("  x: {}".format(x))
    print("  y: {}".format(y))
    print(question_05(x, y))


class Wrapper:
    """ For Question 6. :-) """
    def __init__(self, item, index):
        self.item = item
        self.index = index
    def __str__(self):
        return "(item, index) = ({}, {})".format(self.item, self.index)

def question_06(slist):
    """
    Assumes that we can modify the node items to include a wrapper index.
    Assumes that items can be converted to Wrappers.  If the slist is corrupt,
    return the wrapped item (which gives the original item) If the slist is not
    corrupt, just return None.
    """
    current = slist._head
    if current is None or current._next is None:
        return None

    index = 0
    while current._next is not None:
        if type(current._item) is Wrapper:
            return current._item
        current._item = Wrapper(current._item, index)
        index += 1
        current = current._next

    # If we ever see a next be none, we're done as the list isn't corrupted.
    return -1

def question_06_test():
    print("\n\nQuestion 6 stuff!")

    x = SList()
    x.insert_front(10)
    x.insert_front(7)
    print("    Not corrupt (should return -1).")
    print(x)
    print(question_06(x))

    x = SList()
    corrupt = SListNode(10)
    x._head = corrupt
    x._head._next = SListNode(7)
    x._head._next._next = corrupt
    print("    Corrupt (should return 10).")
    print(question_06(x))


def question_07_slist(slist):
    if slist._head is None:
        return True # vacuously
    slow = slist._head
    fast = slist._head
    first_half = []
    second_half = []
    index = 0
    while fast._next is not None:
        fast = fast._next 
        if index % 2 == 0:
            first_half.append(slow._item)
            slow = slow._next
        index += 1
        if index >= slist._size/2: # depends on python 3
            second_half.append(fast._item)
    return first_half == second_half[::-1]

def question_07(dlist):
    # DLIST VERSION
    index = 0
    left = dlist._sentinel._prev # Advances left
    right = dlist._sentinel._next # Advances right
    while index < int(dlist._size / 2):
        if left._item != right._item:
            return False
        left = left._prev
        right = right._next
        index += 1
    return True


def question_07_test():
    print("\n\nQuestion 7 stuff!")
    d = DList()
    d.insert_front("a")
    print(d)
    print(question_07(d))
    d.insert_front("a")
    print(d)
    print(question_07(d))
    d.insert_front("a")
    print(d)
    print(question_07(d))
    d.insert_front("b")
    print(d)
    print(question_07(d))
    d.remove_last()
    d.remove_last()
    print(d)
    print(question_07(d))
   
    d = DList()
    d.insert_front("s")
    d.insert_front("o")
    d.insert_front("r")
    d.insert_front("r")
    d.insert_front("o")
    d.insert_front("s")
    print(d)
    print(question_07(d))
    print("")

    d = SList()
    d.insert_front("a")
    print(d)
    print(question_07_slist(d))
    d.insert_front("a")
    print(d)
    print(question_07_slist(d))
    d.insert_front("a")
    print(d)
    print(question_07_slist(d))
    d.insert_front("b")
    print(d)
    print(question_07_slist(d))
   
    d = SList()
    d.insert_front("s")
    d.insert_front("o")
    d.insert_front("r")
    d.insert_front("r")
    d.insert_front("o")
    d.insert_front("s")
    print(d)
    print(question_07_slist(d))
    print("")


def intersect(slist1, slist2):
    assert slist1 is not None and slist2 is not None \
            and slist1._head is not None and slist2._head is not None

    def get_tail_size(slist):
        node = slist._head
        size = 1
        while node._next is not None:
            node = node._next
            size += 1
        return (node, size)

    pt1, size1 = get_tail_size(slist1)
    pt2, size2 = get_tail_size(slist2)

    if pt1 is pt2:
        offset = size1 - size2
        # Track node_longer_list and node_shorter_list.
        node_l = slist1._head if offset >= 0 else slist2._head
        node_s = slist1._head if offset < 0 else slist2._head

        # If the offset is zero, the lists are the same length.
        if abs(offset) > 0:
            offset = abs(offset)
            while offset > 0:
                node_l = node_l._next
                offset -= 1

        while node_l is not node_s:
            node_l = node_l._next
            node_s = node_s._next
        return (True, node_l)
    else: 
        return (False, None)


def question_07_ctci6_test():
    x = SList()
    x.insert_front(10)
    x.insert_front(7)
    y = SList()
    y.insert_front(10)
    y.insert_front(7)
    print("\nNon-intersecting case:")
    print("List 1: {}".format(x))
    print("List 2: {}".format(y))
    print(intersect(x,y))

    x = SList()
    y = SList()
    node = SListNode("shared")
    nodex = SListNode("x1", n=node)
    nodey = SListNode("y1", n=node)
    x._head = nodex
    y._head = nodey
    x._size = 2
    y._size = 2
    print("\nNow the intersecting case, same lengths:")
    print("List 1: {}".format(x))
    print("List 2: {}".format(y))
    print(intersect(x,y))
    a,b = intersect(x,y)
    print("  with item: {}".format(b._item))

    x = SList()
    y = SList()
    node_last = SListNode("last")
    node = SListNode("shared", n=node_last)
    nodex2 = SListNode("x2", n=node)
    nodex1 = SListNode("x1", n=nodex2)
    nodey = SListNode("y1", n=node)
    x._head = nodex1
    y._head = nodey
    x._size = 4
    y._size = 3
    print("\nNow the intersecting case, different lengths:")
    print("List 1: {}".format(x))
    print("List 2: {}".format(y))
    print(intersect(x,y))
    a,b = intersect(x,y)
    print("  with item: {}".format(b._item))


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

    # New question from CtCi 6th edition
    question_07_ctci6_test()
