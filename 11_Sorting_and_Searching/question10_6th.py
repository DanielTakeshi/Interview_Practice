""" Testing Question 10.10, ranking. """

class BinaryNode:
    """ The components making up the Binary (Search) Tree. """

    def __init__(self, value, nleft=0):
        self.value = value
        self.nleft = nleft
        self.lchild = None
        self.rchild = None

class BinarySearchTree:
    """ Implements algorithms for the BST. """

    def __init__(self, root):
        self.root = root

    def add_node(self, x):
        if self.root is None:
            self.root = BinaryNode(value=x)
        else:
            node = self.root
            while True:
                if x <= node.value:
                    node.nleft += 1 # important!!
                    if node.lchild is None:
                        node.lchild = BinaryNode(value=x)
                        break
                    node = node.lchild
                else:
                    if node.rchild is None:
                        node.rchild = BinaryNode(value=x)
                        break
                    node = node.rchild

    def get_rank_of_number(self, x):
        if self.root is None:
            return 0
        node = self.root
        done = False
        num_less_equal = 0 # not including itself!!
        
        while not done:
            # Important to have x < val, not x <= val.
            if x == node.value:
                print("in < case with {}, node.value {}".format(num_less_equal,
                        node.value))

                num_less_equal += node.value
                done = True
            elif x < node.value:
                print("in < case with {}, node.value {}".format(num_less_equal,
                        node.value))
                if node.lchild is None:
                    done = True
                else:
                    node = node.lchild
            else:
                print("in > case with {}, node.value {}".format(num_less_equal,
                        node.value))
                # Add +1 since node.value <= x (unless at end)
                # Add node.nleft! That also counts as <= x.
                num_less_equal += (node.nleft)
                if node.rchild is None:
                    done = True
                else:
                    num_less_equal += 1
                    node = node.rchild

        return num_less_equal


class StreamTracker:
    """ 
    Yes, I know I'm just calling the BST ...
    it might be useful to seprate the code for later. 
    """

    def __init__(self):
        self.bst = BinarySearchTree(root=None)

    def track(self, x):
        """ 
        Called each time we see a number; x is an int.  Specifically, assume
        that external code calls this each time we want to add a new integer to
        the stream.  
        """
        self.bst.add_node(x)

    def get_rank_of_number(self, x):
        """ 
        Called periodically; x is an int. Still applies even
        if we've never seen this integer before in the stream!
        (Maybe for simplicity, assume we need to have seen x?)
        """
        return self.bst.get_rank_of_number(x)


if  __name__ == "__main__":
    st = StreamTracker()
    stream = [5,1,4,4,5,9,7,13,3]
    for x in stream:
        st.track(x)
    #for num in stream:
    #    print("rank({}): {}".format(num, st.get_rank_of_number(num)))
    print("rank({}): {}".format(1, st.get_rank_of_number(1)))
