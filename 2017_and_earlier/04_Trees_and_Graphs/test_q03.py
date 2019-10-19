""" Test question 03 for trees. """

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

def case(k):
    vals = [x for x in range(k)]
    print("\nvals = {}\n".format(vals))
    bt = make_bst(vals)
    if bt is not None:
        bt.pretty_print()    

if __name__ == "__main__":
    choices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for k in choices:
        case(k)












































## def make_bst(values):
##     """ A bst of level k contains [2^(k-1), 2^k-1] elements. I.e. we can get
##     2^k-1, but we shouldn't get 2^(k-1)-1 elements, that's the most complete
##     level k-1 bst.  I think the only reason why I have a special case for this
##     is because of my tree design, which needs a special BinaryTree for the root
##     node. This returns (obviously) a BinaryTree.
##     """
##     root_node = make_bst_node(values)
##     return BinaryTree(root=root_node)
## 
## def make_bst_node(values):
##     """ Returns a BinaryNode. Called recursively. With the special 2^k-1 cases,
##     len(values)/2 will round down to be the exact median index, so it's OK.
##     """
##     if len(values) == 0:
##         return None
##     median = len(values)/2
##     lchild = make_bst_node(values[:median])
##     rchild = make_bst_node(values[median+1:])
##     return BinaryNode(item=values[median], lchild=lchild, rchild=rchild)


