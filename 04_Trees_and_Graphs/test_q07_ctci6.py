class Graph:

    def __init__(self, nodes, name_to_index, adj):
        """ 
        Given node name (i.e., item) the self.name_to_index dict
        lets us retrieve the index in the self.nodes list.
        """
        self.nodes = nodes
        self.name_to_index = name_to_index
        self.adj = adj

    def __str__(self):
        string = ""
        for i,n in enumerate(self.nodes):
            string += "  node {}, item {}\nparents: {}\nchildren: {}\n".format(
                    i, n.item, n.children, n.parents, n.visited)
        return string

class Node:

    def __init__(self, item, children=None, parents=None):
        self.item = item
        self.children = children
        self.parents = parents
        self.visited = False

    def __str__(self):
        return str(self.item)

def form_graph(projects, dependencies):
    """ Returns a Graph object representing the data. """

    n = len(projects)
    nodes = []
    name_to_index = {}
    for index,value in enumerate(projects):
        nodes.append(Node(item=value, children=[], parents=[]))
        name_to_index[value] = index

    # Use adj[i][j] for (i) -> (j) edges in the graph.
    # To find children of node i, check all adj[i][:].
    # To find parents of node j, check all adj[:][j].
    # We created n nodes with empty lists, so we'll be appending.
    # And BTW, if a node is stored at nodes[i], its index is i.

    adj = [[0 for _ in range(n)] for _ in range(n)]

    for dep in dependencies:
        node1_idx = name_to_index[dep[0]]
        node2_idx = name_to_index[dep[1]]
        adj[node1_idx][node2_idx] = 1
        node1 = nodes[node1_idx]
        node2 = nodes[node2_idx]
        node1.children.append(node2)
        node2.parents.append(node1)

    return Graph(nodes, name_to_index, adj)


def build_order(projects, dependencies):
    """ 
    For the sake of simplicity, pretend that all nodes are
    represented in all dependencies; if they are not then I
    can simply put them first ...
    """
    graph = form_graph(projects, dependencies)
    print("here's the graph:\n{}\n".format(graph))
    build = []  
    num_nodes = len(graph.nodes)

    # First, visit the stuff without parents.
    for index,n in enumerate(graph.nodes):
        if len(n.parents) == 0:
            build.append(n)
            n.visited = True

    # Iterate until we've visited all children.
    # I know it's better to use a queue and do a BFS-like thing.
    while len(build) < num_nodes:
        for node in graph.nodes:
            can_we_add = True
            for p in node.parents:
                if not p.visited:
                    can_we_add = False
                    break
            if can_we_add:
                build.append(node)
                node.visited = True

    return build


if __name__ == "__main__":
    projects = ['a','b','c','d','f']
    dependencies = [('a','d'),('f','b'),('b','d'),('f','a'),('d','c')]
    print("projects: {}\ndependencies: {}".format(projects, dependencies))
    build = build_order(projects, dependencies)
    for node in build:
        print(node.item)
