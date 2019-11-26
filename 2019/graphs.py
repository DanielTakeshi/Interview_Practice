# The common orderings. For these, assume n is some root node of a
# BINARY tree. That is, we can implement these with this class:

# Because I don't know the standard Python Queue API.
class Queue:

    def __init__(self):
        self.data = []

    def insert(self, item):
        self.data.append(item)

    def pop(self):
        item = self.data[0]
        self.data = self.data[1:]
        return item

    def size(self):
        return len(self.data)


class Graph:

    def __init__(self, nodes=[]):
        self.nodes = nodes

    def __str__(self):
        s = "".format()
        for n in self.nodes:
            s += "{} : {}\n".format(n.name, n.neighbors)
        return s

    def _reset(self):
        for n in self.nodes:
            n.visited = False

    def _visit(self, n):
        print('{}'.format(n))

    def bfs(self, start_node):
        """A visited node is one that is *added* to the frontier.

        So far, it's passing all my tests...
        """
        self._reset()
        frontier = Queue()
        frontier.insert(start_node)
        start_node.visited = True
        while frontier.size() != 0:
            n = frontier.pop()
            self._visit(n)
            for nbor in n.neighbors:
                if not nbor.visited:
                    frontier.insert(nbor)
                    nbor.visited = True

    def dfs(self, start_node):
        """We could have also just made a Stack class.

        The list class already has a pop() method that does this:

            n = frontier[-1]
            frontier = frontier[:-1]

        Gayle solution is recursive, and she doesn't need the extra `if not
        n.visited` case that I have to do before calling _visit(). It's a bit
        tricky, easiest to work it out through a cycle, like a graph with:
        (A-B-C-D-A) graph.

        So far, it's passing all my tests... and it matches the Wiki code:

            https://en.wikipedia.org/wiki/Depth-first_search

        where, yes, they delay checking for visitation until we pop fron the
        frontier. That is critical!! Actually if you note, I don't even need
        the second `if not nbor.visited` line because that will simply add
        visited nodes to the frontier, and the first call to check for
        visitation will catch that (right after the popping).
        """
        self._reset()
        frontier = [start_node]
        while len(frontier) != 0:
            n = frontier.pop()
            if not n.visited:
                self._visit(n)
                for nbor in n.neighbors:
                    if not nbor.visited:
                        frontier.append(nbor)
                n.visited = True


class Node:

    def __init__(self, name, neighbors=[]):
        self.name = name
        self.neighbors = neighbors
        self.visited = False

    def __str__(self):
        s = "{}".format(self.name)
        return s


def graph01():
    n1 = Node('A')
    nodes = [n1]
    return Graph(nodes=nodes)

def graph02():
    """
    Fully connected.
    """
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n1.neighbors = [n2,n3]
    n2.neighbors = [n1,n3]
    n3.neighbors = [n1,n2]
    nodes = [n1, n2, n3]
    return Graph(nodes=nodes)

def graph03():
    """
    This is D - B - A - C - E, A as 'root' effectively.
    """
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n1.neighbors = [n2,n3]
    n2.neighbors = [n1,n4]
    n3.neighbors = [n1,n5]
    n4.neighbors = [n2]
    n5.neighbors = [n3]
    nodes = [n1, n2, n3, n4, n5]
    return Graph(nodes=nodes)

def graph04():
    """
    This is a loop, A - B - D - E - C - A, etc.
    """
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n1.neighbors = [n2,n3]
    n2.neighbors = [n1,n4]
    n3.neighbors = [n1,n5]
    n4.neighbors = [n2,n5]
    n5.neighbors = [n3,n4]
    nodes = [n1, n2, n3, n4, n5]
    return Graph(nodes=nodes)

def graph05():
    """
    Loop of A - B - D - E - C - A, and then with F 'jutting' out of E.
    """
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n6 = Node('F')
    n1.neighbors = [n2,n3]
    n2.neighbors = [n1,n4]
    n3.neighbors = [n1,n5]
    n4.neighbors = [n2,n5]
    n5.neighbors = [n3,n4,n6]
    n6.neighbors = [n5]
    nodes = [n1, n2, n3, n4, n5, n6]
    return Graph(nodes=nodes)

def graph03_dir():
    """
    D <-- B <-- A --> C --> E
    """
    n1 = Node('A')
    n2 = Node('B')
    n3 = Node('C')
    n4 = Node('D')
    n5 = Node('E')
    n1.neighbors = [n2,n3]
    n2.neighbors = [n4]
    n3.neighbors = [n5]
    n4.neighbors = []
    n5.neighbors = []
    nodes = [n1, n2, n3, n4, n5]
    return Graph(nodes=nodes)


def test_bfs_dfs():
    """Test DFS and BFS."""
    graphs = [graph01(), graph02(), graph03(), graph04(), graph05()]

    for gidx,g in enumerate(graphs):
        print('\n---------------- ON GRAPH {} ----------------\nBFS:'.format(gidx))
        print('start node: {}'.format(g.nodes[0]))
        g.bfs(g.nodes[0])
        print('start node: {}'.format(g.nodes[-1]))
        g.bfs(g.nodes[-1])

        print('\nnow DFS:')
        print('start node: {}'.format(g.nodes[0]))
        g.dfs(g.nodes[0])
        print('start node: {}'.format(g.nodes[-1]))
        g.dfs(g.nodes[-1])
    print()


## -------------------------------------------------------------------- ##
## -------------------------------------------------------------------- ##
## ------------------------ NOW DOING PROBLEMS ------------------------ ##
## -------------------------------------------------------------------- ##
## -------------------------------------------------------------------- ##

## ------------------------ PROBLEM 01 ------------------------ ##


# Assume we use the same graph class structure as above.
# With directed, we assume if n1 -> n2, then n1.neighbors includes n2.
# But, n2.neighbors does not include n1, UNLESS there are two directed edges.
# Also we only handle n1 -> n2. For the other case, call the function again!
# Remember that any node ADDED to the frontier has been visited!
# Time complexity is the normal time complexity of BFS, which is, I think,
# O(M+N) for M edges and N nodes.

def route(graph, n1, n2):
    # Assumes that checking for equality can be done like this.
    # (I think this tests for equality if they occupy same memory address)
    if n1 == n2:
        return True

    for node in graph.nodes:
        node.visited = False
    frontier = Queue()
    frontier.insert(n1)
    n1.visited = True

    while frontier.size() != 0:
        n = frontier.pop()
        if n == n2:
            return True
        # These are only from n -> nbor, not nbor -> n.
        # By assumption of our class structure. Though even if
        # nbor -> n is part of graph, we'll have already visited!
        for nbor in n.neighbors:
            if not nbor.visited:
                frontier.insert(nbor)
                nbor.visited = True

    # If we got to here, we never caught the target.
    return False


## ------------------------ PROBLEM 02 ------------------------ ##

## ------------------------ PROBLEM 03 ------------------------ ##

## ------------------------ PROBLEM 04 ------------------------ ##

## ------------------------ PROBLEM 05 ------------------------ ##

## ------------------------ PROBLEM 06 ------------------------ ##

## ------------------------ PROBLEM 07 ------------------------ ##

## ------------------------ PROBLEM 08 ------------------------ ##

## ------------------------ PROBLEM 09 ------------------------ ##

## ------------------------ PROBLEM 10 ------------------------ ##

## ------------------------ PROBLEM 11 ------------------------ ##

## ------------------------ PROBLEM 12 ------------------------ ##


if __name__ == "__main__":
    if True:
        # ----------------- Debug BFS and DFS ----------------
        print('-'*120)
        print('ON DEBUGGING and TESTING BFS/DFS')
        print('-'*120)
        test_bfs_dfs()

    if False:
        # ----------------- Problem 01 ----------------
        print('-'*120)
        print('ON PROBLEM 4.01')
        print('-'*120)
        # NOTE: all the ones from the debugging trial used connected graph.  If
        # we assume that those are 'doubled' edges in bidirectional graphs.
        # then all should return True. They do! :-)
        graphs = [graph02(), graph03(), graph04(), graph05(),
                graph03_dir()]

        for gidx,g in enumerate(graphs):
            print('\n---------------- ON GRAPH {} ----------------\n'.format(gidx))
            n1 = g.nodes[0]
            n2 = g.nodes[-1]
            print('Testing if path from: {} --> {}'.format(n1, n2))
            print('route?  {}'.format(route(g, n1, n2)))

            n1 = g.nodes[-1]
            n2 = g.nodes[0]
            print('Testing if path from: {} --> {}'.format(n1, n2))
            print('route?  {}'.format(route(g, n1, n2)))
        print()
