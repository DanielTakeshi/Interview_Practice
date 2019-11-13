# The common orderings. For these, assume n is some root node of a
# BINARY tree. That is, we can implement these with this class:

class Node:

    def __init__(self, item=None, lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild


def in_order(n, spaces=0):
    if n is not None:
        in_order(n.lchild, spaces=spaces+1)
        print(' '*spaces + str(n.item))
        in_order(n.rchild, spaces=spaces+1)

def pre_order(n, spaces=0):
    if n is not None:
        print(' '*spaces + str(n.item))
        pre_order(n.lchild, spaces=spaces+1)
        pre_order(n.rchild, spaces=spaces+1)

def post_order(n, spaces=0):
    if n is not None:
        post_order(n.lchild, spaces=spaces+1)
        post_order(n.rchild, spaces=spaces+1)
        print(' '*spaces + str(n.item))


def tree01():
    n1 = Node(2)
    return n1

def tree02():
    n3 = Node(5)
    n2 = Node(4)
    n1 = Node(3, n2, n3)
    return n1

def tree03():
    n3 = Node(5)
    n2 = Node(4)
    n1 = Node(3, n2, n3)
    return n1

def tree04():
    n5 = Node(5)
    n4 = Node(4)
    n3 = Node(3)
    n2 = Node(2, n4, n5)
    n1 = Node(1, n2, n3)
    return n1

## -------------------------------------------------------------------- ##
## -------------------------------------------------------------------- ##
## ------------------------ NOW DOING PROBLEMS ------------------------ ##
## -------------------------------------------------------------------- ##
## -------------------------------------------------------------------- ##

## ------------------------ PROBLEM 01 ------------------------ ##

## ------------------------ PROBLEM 02 ------------------------ ##

## ------------------------ PROBLEM 03 ------------------------ ##

## ------------------------ PROBLEM 04 ------------------------ ##

## ------------------------ PROBLEM 05 ------------------------ ##


class Node_P5:
    def __init__(self, item, lchild=None, rchild=None):
        self.item = item
        self.lchild = lchild
        self.rchild = rchild
        self.min_subtree = None
        self.max_subtree = None
        self.bst_below = None

    def pretty_print(self, tabstr):
        string = '{}{} (mins: {}, maxs: {}, balanced: {})'.format(
                tabstr, self.item, self.min_subtree, self.max_subtree,
                self.bst_below)
        print(string)


def pretty_print_full(node, tabstr=""):
    if node != None:
        node.pretty_print(tabstr)
        pretty_print_full(node.rchild, tabstr+"\t")
        pretty_print_full(node.lchild, tabstr+"\t")


def validate_bst(n):
    """Assumptions: equality allowed for left hand side sub-branch.

    n: type `Node`, represents the root.
    """
    compute_bst_stuff(n)
    return n.bst_below


def compute_bst_stuff(n):
    if n is not None:
        compute_bst_stuff(n.lchild)
        compute_bst_stuff(n.rchild)

        if n.lchild is None and n.rchild is None:
            # We are at a leaf node. Handle this case right away.
            n.max_subtree = n.item
            n.min_subtree = n.item
            n.bst_below = True
            return

        # Left child case handling.
        if n.lchild is not None:
            max_l_subtree = n.lchild.max_subtree
            if max_l_subtree > n.item or (not n.lchild.bst_below):
                n.bst_below = False

        # Now right child.
        if n.rchild is not None:
            min_r_subtree = n.rchild.min_subtree
            if min_r_subtree <= n.item or (not n.rchild.bst_below):
                n.bst_below = False

        # At this point we know we have a binary search tree if we haven't made
        # false, i.e., if this is None.
        if n.bst_below is None:
            n.bst_below = True

        # Update current node's max/min so it propagates correctly. Should be
        # called even if we're at a non-bst case.
        if n.lchild is not None:
            n.min_subtree = n.lchild.min_subtree
        else:
            n.min_subtree = n.item
        if n.rchild is not None:
            n.max_subtree = n.rchild.max_subtree
        else:
            n.max_subtree = n.item


def p05_tree01():
    n1 = Node_P5(3)
    return n1

def p05_tree02():
    n3 = Node_P5(5)
    n2 = Node_P5(4)
    n1 = Node_P5(3, n2, n3)
    return n1

def p05_tree03():
    n3 = Node_P5(5)
    n2 = Node_P5(-1)
    n1 = Node_P5(3, n2, n3)
    return n1

def p05_tree04():
    n7 = Node_P5(3)
    n6 = Node_P5(1)
    n5 = Node_P5(2, n6, n7)
    n3 = Node_P5(4, n5, None)
    n1 = Node_P5(-1, None, n3)
    return n1

def p05_tree05():
    n7 = Node_P5(5)
    n6 = Node_P5(1)
    n5 = Node_P5(2, n6, n7)
    n3 = Node_P5(4, n5, None)
    n1 = Node_P5(-1, None, n3)
    return n1

## ------------------------ PROBLEM 06 ------------------------ ##

## ------------------------ PROBLEM 07 ------------------------ ##

## ------------------------ PROBLEM 08 ------------------------ ##

## ------------------------ PROBLEM 09 ------------------------ ##

## ------------------------ PROBLEM 10 ------------------------ ##

## ------------------------ PROBLEM 11 ------------------------ ##

## ------------------------ PROBLEM 12 ------------------------ ##



if __name__ == "__main__":
    pass
    # ----------------- Debug trees/graphs ----------------
    trees = [tree01(), tree02(), tree03(), tree04()]
    for t in trees:
        print('\nOn this tree! Inorder, preorder, postorder')
        print('\ninorder')
        in_order(t)
        print('\npreorder')
        pre_order(t)
        print('\npostorder')
        post_order(t)
    print()

    # ----------------- Problem 05 ----------------
    print('-'*120)
    print('ON PROBLEM NUMBER FIVE')
    print('-'*120)

    trees = [p05_tree01(), p05_tree02(), p05_tree03(), p05_tree04(), p05_tree05()]
    for t in trees:
        print('\nNEW TREE. Before\n')
        pretty_print_full(t)
        res = validate_bst(t)
        print('\nafter:\n')
        pretty_print_full(t)
        print('\nbst: {}'.format(res))
    print()
