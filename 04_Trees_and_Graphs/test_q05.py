""" Test question 05 for trees. """

from trees import BinaryTree
from trees import BinaryNode


def make_bst(vals):
    """ `vals` is a list of sorted numbers """
    bst = BinaryTree()
    bst.root = make_balanced_bst(n=None, vals=vals)
    return bst

def make_balanced_bst(n, vals):
    if len(vals) == 0:
        return None
    mid = int(len(vals)/2)
    node = BinaryNode(item=vals[mid], parent=n)
    node.lchild = make_balanced_bst(n=node, vals=vals[:mid])
    node.rchild = make_balanced_bst(n=node, vals=vals[mid+1:])
    return node

##########################
## THE ACTUAL QUESTION ##
##########################

## def is_bst(bt):
##     assert type(bt) is BinaryTree
##     return is_bst_recursive(n=bt.root)
## 
## def is_bst_recursive(n):
##     """ Returns whether n is a b-SEARCH tree or not. """
##     # Note: this is incorrect. Gah, a simple error ...
##     # Also we can still just return a boolean. It's just that we need the min
##     # and max values as second and third parameters in this recursive call.
##     if n.lchild is None and n.rchild is None:
##         return True
##     if n.lchild is None:
##         r_isbst = is_bst_recursive(n=n.rchild)
##         return (n.item <= n.rchild.item and r_isbst)
##     if n.rchild is None:
##         l_isbst = is_bst_recursive(n=n.lchild)
##         return (n.lchild.item <= n.item and l_isbst)
##     else:
##         l_isbst = is_bst_recursive(n=n.lchild)
##         r_isbst = is_bst_recursive(n=n.rchild)
##         return ((n.lchild.item <= n.item <= n.rchild.item) and \
##                     l_isbst and r_isbst)

def is_bst(bt):
    import numpy as np
    return is_bst_node(bt.root, np.float('-inf'), np.float('inf'))

def is_bst_node(n, min, max):
    if n is None:
        return True
    if not (min <= n.item <= max):
        return False 
    return is_bst_node(n.lchild, min, n.item) and \
           is_bst_node(n.rchild, n.item, max)


if __name__ == "__main__":
    choices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for k in choices:
        vals = [x for x in range(k)]
        if len(vals) == 0: continue
        print("\nvals = {}\n".format(vals))
        bt = make_bst(vals)
        bt.pretty_print()    
        print("IS IT A BINARY SEARCH TREE? {}".format(is_bst(bt)))

    print("\nNow some false cases.")
    bt = BinaryTree()
    bt.root = BinaryNode(3)
    bt.root.lchild = BinaryNode(2)
    bt.root.lchild.lchild = BinaryNode(-20)
    bt.root.lchild.rchild = BinaryNode(20)
    bt.root.rchild = BinaryNode(10)
    bt.pretty_print()
    print("IS IT A BINARY SEARCH TREE? {}".format(is_bst(bt)))
