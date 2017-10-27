""" Test question 04 for trees. """

from trees import BinaryTree
from trees import BinaryNode
from stack_queue import Queue  # My old code so I can use a BFS.

# I re-implemented these for practice. :-)

class SList:
    def __init__(self, head=None):
        self._head = head
    def insert_front(self, item):
        self._head= SListNode(i=item, n=self._head)
    def __str__(self):
        """ OK fine I copied this one ..."""
        l_str = "[head] -> " + str(self._head._item)
        node = self._head
        while node._next != None:
            node = node._next
            l_str += " -> " + str(node._item)
        return l_str + " -> [None]"

class SListNode:
    def __init__(self, i=None, n=None):
        self._item = i
        self._next = n


# Older code

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


# Now the actual core of the question.

def get_linked_lists(bt):
    """ 
    Given bt, run BFS. Each layer gets its linked list.  For simplicity assume
    nodes have a `visited` flag.  And a `height` flag. Or just make a wrapper.
    """
    frontier = Queue()
    frontier.enqueue( (bt.root,0) ) # Only _un-visited_ nodes!
    linked_lists = []

    while (frontier.first is not None):
        node,height = frontier.dequeue()
        node.visited = True
        while len(linked_lists) <= height:
            linked_lists.append( SList() )
        linked_lists[height].insert_front( node )

        # Some of this is not necessary for a binary tree
        # But I wanted to maintain some connection to BFS.
        # In a binary tree we don't need to check `visited`.
        if node.lchild is not None and not node.lchild.visited:
            frontier.enqueue( (node.lchild, height+1) )
        if node.rchild is not None and not node.rchild.visited:
            frontier.enqueue( (node.rchild, height+1))

    return linked_lists

if __name__ == "__main__":
    choices = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    for k in choices:
        vals = [x for x in range(k)]
        if len(vals) == 0: continue
        print("\nvals = {}".format(vals))
        bt = make_bst(vals)
        print("\nHere's the pretty print:")
        bt.pretty_print()    
        print("\nHere are the linked lists for these:")
        lls = get_linked_lists(bt)
        for ll in lls:
            print(ll)
