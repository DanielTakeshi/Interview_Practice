""" Practice implementing from scratch. """


from collections import defaultdict
from queue import Queue

class Node:

    def __init__(self, item, parents=None, children=None):
        self.item = item 
        self.parents = parents
        self.children = children
        self.visited = False # For graph traversals

    def __str__(self):
        res = str(self.item)
        return res


class Graph:

    def __init__(self, nodes, edges):
        """ 
        Assumes nodes is a list of hashable items. Assumes edges
        is a list of tuples (of those items).
        """
        # do error checking code (skipping for simplicity)
        self.N = len(nodes)
        self.adj_m = [[0 for _ in range(self.N)] for _ in range(self.N)]
        self.adj_l = [[] for _ in range(self.N)]
        self.nodes_to_idx = {} # Hash the node ITEM!!

        # Might be handy to have self.nodes around for indexing.  Use
        # this to go from integer index to node item.
        # Alternative: have Node class retain index as a field.
        self.nodes = []
        idx = 0
        for node in nodes:
            assert node not in self.nodes_to_idx
            self.nodes_to_idx[node] = idx
            idx += 1
            self.nodes.append(Node(item=node))

        for edge in edges:
            item1, item2 = edge
            assert item1 != item2
            u = self.nodes_to_idx[item1]
            v = self.nodes_to_idx[item2]
            self.adj_m[u][v] = 1
            self.adj_m[v][u] = 1
            self.adj_l[u].append(v)
            self.adj_l[v].append(u)


    def dfs(self, item):
        """ Easiest to do this with a stack. """
        start_node = None
        for node in self.nodes:
            node.visited = False
            if node.item == item:
                start_node = node
        assert start_node is not None

        frontier = [start_node]
        while len(frontier) > 0:
            node = frontier.pop()
            node.visited = True
            print("visiting node: {}".format(node))
            idx = self.nodes_to_idx[node.item]
            for index in self.adj_l[idx]:
                neighbor = self.nodes[index]
                if not neighbor.visited:
                    frontier.append(neighbor)

    def bfs(self, item):
        start_node = None
        for node in self.nodes:
            node.visited = False
            if node.item == item:
                start_node = node
        assert start_node is not None

        q = Queue()
        q.put((start_node, 1))

        while not q.empty():
            node, level = q.get()
            node.visited = True
            print("visiting node: {} at level {}".format(node,level))
            level += 1   
            idx = self.nodes_to_idx[node.item]
            for index in self.adj_l[idx]:
                neighbor = self.nodes[index]
                if not neighbor.visited:
                    q.put((neighbor,level))

    def __str__(self):
        s = "Nodes_to_indices:\n"
        s += str(self.nodes_to_idx)
        s += "\n\nAdj_M:\n"
        for row in self.adj_m:
            s += str(row)+"\n"
        s += "\nAdj_L:\n"
        for idx,l in enumerate(self.adj_l):
            s += "{:10} {}\n".format(self.nodes[idx].item, l)
        return s


if __name__ == "__main__":
    nodes = ["alice", "bob", "christine", "daniel", "eiko", "fred"]
    edges = [
        ("alice", "bob"),
        ("christine", "daniel"),
        ("bob", "daniel"),
        ("daniel", "eiko"),
        ("alice", "fred")
    ]
    g = Graph(nodes, edges)
    print(g)

    print("\nDFS:")
    for item in nodes:
        print("\n\tstarting node: {}".format(item))
        g.dfs(item)

    print("\nBFS:")
    for item in nodes:
        print("\n\tstarting node: {}".format(item))
        g.bfs(item)
