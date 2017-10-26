""" Finding in-order successor. Heck, let's do the traversals here! """
from trees import BinaryNode, BinaryTree

def inorder(bnode):
    if bnode.lchild is not None:
        inorder(bnode.lchild)
    print("{} ".format(bnode.item), end='')
    if bnode.rchild is not None:
        inorder(bnode.rchild)

def preorder(bnode):
    print("{} ".format(bnode.item), end='')
    if bnode.lchild is not None:
        preorder(bnode.lchild)
    if bnode.rchild is not None:
        preorder(bnode.rchild)

def postorder(bnode):
    if bnode.lchild is not None:
        postorder(bnode.lchild)
    if bnode.rchild is not None:
        postorder(bnode.rchild)
    print("{} ".format(bnode.item), end='')


## def inorder_successor(node, return_itself=False):
##     # If the parent is None, we know we're at the root. Go right.
##     # We MAY have to return nothing! If it's imbalanced.
##     if node.parent is None:
##         if node.rchild is not None:
##             return inorder_successor(node.rchild, return_itself=True)
##         else:
##             if return_itself:
##                 return node
##             else:
##                 # no successor, as this was the original node called.
##                 return None 
##     p = node.parent
## 
##     if p.rchild is not None and node is p.rchild:
##         # Current node is the right child of p.
##         if node.rchild is not None:
##             return inorder_successor(node.rchild, return_itself=True)
##         else:
##             if return_itself:
##                 return node
##             else:
##                 # no successor as this was the original node called.
##                 return None 
##     else:
##         # Current node is the left child of p.
##         if node.rchild is not None:
##             return inorder_successor(node.rchild, return_itself=True)
##         else:
##             return inorder_successor(p)


def inorder_successor(node, ignore_right=False):
    # Recurse until we get to some right child branch.
    # If there's no right child, then there are several cases.
    # Might be no successor. Or go back up to the parent.
    # If this was a left child, and we go up to the parent, we're done!
    if node.rchild is None or ignore_right:
        if node.parent is None:
            return None
        elif node is node.parent.lchild:
            return node.parent
        else:
            return inorder_successor(node.parent, True)   
    else: 
        return get_leftmost(node.rchild)

def get_leftmost(node):
    """ Returns leftmost node in subtree rooted at node. """
    if node.lchild is None:
        return node
    else:
        return get_leftmost(node.lchild)


if __name__ == "__main__":
    bt = BinaryTree()
    bt.root = BinaryNode(item=1)
    bt.root.lchild = BinaryNode(item=2, parent=bt.root)
    bt.root.rchild = BinaryNode(item=3, parent=bt.root)

    bt.root.lchild.lchild = BinaryNode(item=4, parent=bt.root.lchild)
    bt.root.lchild.rchild = BinaryNode(item=5, parent=bt.root.lchild)

    bt.root.rchild.lchild = BinaryNode(item=6, parent=bt.root.rchild)
    bt.root.rchild.rchild = BinaryNode(item=7, parent=bt.root.rchild)

    # For now assume bt.root itself is not None.
    print("\nHere's the tree, and inorder/preorder/postorder traversals ...")
    bt.pretty_print()
    inorder(bt.root)
    print(" (Inorder)")
    preorder(bt.root)
    print(" (Preorder)")
    postorder(bt.root)
    print(" (Postorder)")

    print("\nNow testing question 6...")
    print("root successor {}".format(bt.root))
    print(inorder_successor(bt.root))

    print("root.lchild successor {}".format(bt.root.lchild))
    print(inorder_successor(bt.root.lchild))
    print("root.rchild successor {}".format(bt.root.rchild))
    print(inorder_successor(bt.root.rchild))

    print("root.lchild.lchild {}".format(bt.root.lchild.lchild))
    print(inorder_successor(bt.root.lchild.lchild))
    print("root.lchild.rchild {}".format(bt.root.lchild.rchild))
    print(inorder_successor(bt.root.lchild.rchild))

    print("root.rchild.lchild {}".format(bt.root.rchild.lchild))
    print(inorder_successor(bt.root.rchild.lchild))
    print("root.rchild.rchild {}".format(bt.root.rchild.rchild))
    print(inorder_successor(bt.root.rchild.rchild))
