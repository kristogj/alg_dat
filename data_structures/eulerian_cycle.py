class Node(object):
    def __init__(self, value):
        self.value = value
        self.edges = []
        self.visited = False


class Edge(object):
    def __init__(self, value, node_from, node_to):
        self.value = value
        self.node_from = node_from
        self.node_to = node_to


class Graph(object):
    def __init__(self, nodes=None, edges=None):
        self.nodes = nodes or []
        self.edges = edges or []


    def get_adjacency_list(self):
        """Return a list of lists.
        The indecies of the outer list represent "from" nodes.
        Each section in the list will store a list
        of tuples that looks like this:
        (To Node, Edge Value)"""
        max_index = self.find_max_index() + 1
        adjacency_list = [[] for _ in range(max_index)]
        for edg in self.edges:
            from_value, to_value = edg.node_from.value, edg.node_to.value
            # This graph does not have directed edges
            adjacency_list[from_value].append((to_value, edg.value))
            adjacency_list[to_value].append((from_value,edg.value))
        return [a or None for a in adjacency_list]  # replace []'s with None

    def find_max_index(self):
        """Return the highest found node number
        Or the length of the node names if set with set_node_names()."""
        max_index = -1
        if len(self.nodes):
            for node in self.nodes:
                if node.value > max_index:
                    max_index = node.value
        return max_index


    """
    We have an eulerian cycle if each node in the graph has an even degree of edges for it
    """
    def has_eulerian_cycle(self):
        adj_list = self.get_adjacency_list()
        for edges in adj_list:
            if edges:
                if len(edges) % 2 != 0:
                    return False
        return True


n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
e1 = Edge(1,n1,n2)
e2 = Edge(1,n1,n4)
e3 = Edge(1,n2,n3)
e4 = Edge(1,n3,n4)
e5 = Edge(1,n2,n4)

# Should be True
g1 = Graph([n1,n2,n3,n4],[e1,e2,e3,e4])
print(g1.has_eulerian_cycle())

# Should be False
g2 = Graph([n1,n2,n3,n4],[e1,e2,e3,e4,e5])
print(g2.has_eulerian_cycle())

