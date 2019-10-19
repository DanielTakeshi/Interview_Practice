class Node:
    def __init__(self, item=None, next=None):
        self.item = item
        self.next = next

    def __str__(self):
        s = '[{}] --> {}'.format(self.item, self.next)
        return s


def test01():
    n3 = Node(3)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    return n1


def test02():
    n3 = Node(1)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    return n1


def test03():
    n2 = Node(1)
    n1 = Node(1, n2)
    return n1


def test04():
    n6 = Node(1)
    n5 = Node(2, n6)
    n4 = Node(3, n5)
    n3 = Node(2, n4)
    n2 = Node(2, n3)
    n1 = Node(1, n2)
    return n1


def test05():
    n2 = Node(1)
    n1 = Node(3, n2)
    return n1


def test06():
    n1 = Node(3)
    return n1


def test07():
    n5 = Node(4)
    n4 = Node(4, n5)
    n3 = Node(4, n4)
    n2 = Node(4, n3)
    n1 = Node(4, n2)
    return n1



## ------------------------ PROBLEM 01 ------------------------ ##

def remove_duplicates_1(node):
    """Assumes node is not None.

    Assumes we're OK with first item of duplicates remaining.  So we only
    remove the ones after the first appearance.  Where 'first' is based on
    close-ness to `node`.

    Assumes a temporary buffer `values`. So it's O(N) time.  Also O(N) space.
    """
    values = set()
    curr = node
    while (curr.next is not None):
        # assumes we're at curr.item and it is NOT a duplicate
        values.add(curr.item)
        while (curr.next is not None and curr.next.item in values):
            curr.next = curr.next.next
        if curr.next is not None:
            curr = curr.next


def remove_duplicates_2(node):
    """Assumes node is not None.

    Assumes we're OK with first item of duplicates remaining.  So we only
    remove the ones after the first appearance.  Where 'first' is based on
    close-ness to `node`.

    Now does not allow for a temporary buffer, so it's O(N^2) time.
    """
    curr = node
    #runn = node

    while (curr.next is not None):
        val_to_del = curr.item
        runn = curr

        while (runn.next is not None):
            if runn.next.item == val_to_del:
                runn.next = runn.next.next
            else:
                runn = runn.next

        if curr.next is not None:
            curr = curr.next


## ------------------------ PROBLEM 02 ------------------------ ##

def k_th_last(node, k):
    """k-th to last. Assumptions:

    - Don't do anything if k < 1

    - If k=1, that is the same as removing the LAST item.

    - Thus if k=2, we remove second to last, etc.

    - if list has exactly k items, we leave as it is because otherwise we need
      a reference to the original node, e.g.: [1]->[2]->None, for k=2 we need
      to remove [1] but we have only a singly linked list and we start with [1]
      and its next node, so we can't remove [1] unless we have extra
      info.

    Note: I actually misread the question, I thought she wanted me to remove
    the k-th to last, which is not possible with exactly length k items. I get
    it now.
    """
    if k < 1:
        return
    curr = node
    runn = node

    # after this, runner is k nodes ahead of current (or exit)
    count = 0
    while count < k:
        if runn is None:
            return  # don't have k items
        runn = runn.next
        count += 1

    # handle special case of len k list. Or return this node exactly
    # if the goal is to RETURN the item and not modify the list.
    if runn is None:
        return

    # go to end, at that point curr is pointing a node such that
    # the node's NEXT field points at the 'kth-to-last' node.
    while runn.next is not None:
        runn = runn.next
        curr = curr.next

    curr.next = curr.next.next


## ------------------------ PROBLEM 03 ------------------------ ##

## ------------------------ PROBLEM 04 ------------------------ ##

## ------------------------ PROBLEM 05 ------------------------ ##

## ------------------------ PROBLEM 06 ------------------------ ##

## ------------------------ PROBLEM 07 ------------------------ ##



if __name__ == "__main__":
    # ----------------- Problem 01 (v1) ----------------
    print('')
    print('-'*120)
    print('PROBLEM 1, FIRST VERSION\n')
    lists = [test01(), test02(), test03(), test04(), test05(), test06(), test07()]
    for n in lists:
        print('Before: {}'.format(n))
        remove_duplicates_1(n)
        print('After:  {}\n'.format(n))

    # ----------------- Problem 01 (v1) ----------------
    print('')
    print('-'*120)
    print('PROBLEM 1, SECOND VERSION\n')
    lists = [test01(), test02(), test03(), test04(), test05(), test06(), test07()]
    for n in lists:
        print('Before: {}'.format(n))
        remove_duplicates_2(n)
        print('After:  {}\n'.format(n))

    # ----------------- Problem 02 ----------------
    print('')
    print('-'*120)
    print('PROBLEM 2\n')
    for k in range(1,5):
        lists = [test01(), test02(), test03(), test04(), test05(), test06(), test07()]
        for n in lists:
            print('Before (k={}): {}'.format(k, n))
            k_th_last(n, k)
            print('After  (k={}): {}\n'.format(k, n))
