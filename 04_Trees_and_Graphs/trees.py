""" Defining trees, to keep methods here. """

class BinaryNode:

    def __init__(self, item=None, parent=None, lchild=None, rchild=None):
        self.item = item
        self.parent = parent
        self.lchild = lchild
        self.rchild = rchild
        self.height = None
        self.balanced = None
        self.visited = False

    def _pretty_print(self, tabstr):
        if self.height != None and self.balanced != None:
            print(tabstr + "("+str(self.item)+", "+str(self.height)+", "+\
                    str(self.balanced)+")")
        else:
            print(tabstr + str(self.item))

    def __str__(self):
        return "[{}]".format(self.item)

class BinaryTree:

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

    ###
    # Stuff for answering coding questions
    ###

    def _assign_heights_and_balance(self, n):
        """ For question 01. """
        if n.lchild is None and n.rchild is None:
            n.height = 0
            n.balanced = True
        elif n.lchild is None:
            self._assign_heights_and_balance(n = n.rchild)
            n.height = n.rchild.height + 1
            n.balanced = (n.height == 1)
        elif n.rchild is None:
            self._assign_heights_and_balance(n = n.lchild)
            n.height = n.lchild.height + 1
            n.balanced = (n.height == 1)
        else:
            self._assign_heights_and_balance(n = n.lchild)
            self._assign_heights_and_balance(n = n.rchild)
            lh = n.lchild.height
            rh = n.rchild.height
            n.height = max(lh,rh) + 1
            n.balanced = abs(lh-rh) <= 1

    def is_balanced(self):
        """ Calls helper method to assign height/balanced to each node. """
        assert self.root is not None
        self._assign_heights_and_balance(n=self.root)
        return self.root.balanced
