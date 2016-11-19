"""
Defining trees, to keep methods here.
"""

class BinaryTree:
    """ It helps to have a reference to the root. """

    def __init__(self, root=None, size=None):
        self.root = root
        self.size = size

    def pretty_print(self):
        self._pretty_print(self.root, "")

    def _pretty_print(self, node, tabstr):
        """ Print right first then left, due to way unix prints them. """
        if node != None:
            node._pretty_print(tabstr)
            self._pretty_print(node.rchild, tabstr+"\t")
            self._pretty_print(node.lchild, tabstr+"\t")

    def dfs(self, node):
        """ In BinaryTree class, this will run DFS with some arbitrary node as input. """
        if node.lchild != None:
            self.dfs(node.lchild)
        if node.rchild != None:
            self.dfs(node.rchild)
        (node.height, node.balanced) = self.height_and_balance(node)

    def height_and_balance(self, node):
        """ Computes height of node, from dfs call.  Assumes the invariant: that
        all children (if any) have heights computed beforehand. This will ALSO
        check to see if the nodes are balanced!! So it returns a tuple. """

        if node.lchild == None and node.rchild == None:
            return (0,True)
        if node.lchild == None:
            h = node.rchild.height
            balanced = (h == 0)
            return (h+1, balanced)
        if node.rchild == None:
            h = node.lchild.height
            balanced = (h == 0)
            return (h+1, balanced)

        h1 = node.lchild.height
        h2 = node.rchild.height
        balanced = (abs(h1 - h2) <= 1)
        return (max(h1,h2) + 1, balanced)

    def is_balanced(self):
        """ First, it runs dfs to get the distances. Then we check. """
        if self.root == None:
            return True
        self.dfs(self.root)
        return self.root.balanced


class BinaryNode:
    """ These make up the BinaryTree objects. """

    def __init__(self, item=None, parent=None, lchild=None, rchild=None):
        self.item = item
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild
        self.height = None
        self.balanced = None

    def _pretty_print(self, tabstr):
        if self.height != None and self.balanced != None:
            print(tabstr + "("+str(self.item)+", "+str(self.height)+", "+str(self.balanced)+")")
        else:
            print(tabstr + str(self.item))
