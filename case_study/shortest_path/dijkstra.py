from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt
import random

class Node:

    def __init__(self,id):
        self.id = id
        self.distance = float('inf')
        self.parent = None

    def __str__(self):
        return f"(ID: {self.id}, D: {self.distance}, BEST_P: {self.parent})"

    def __repr__(self):
        return f"ID: {self.id}"

class Graph:

    def __init__(self):
        self.nodes = set()
        """
        The reason I use defaultdict is that I do not have to init an empty list if no values has been appended yet
        I set the default to be an empty list right away, so i will never get an error when appending with a key
        i never have used
        example: defaultdict(<class 'list'>, {4: [3, 5]})
        """
        self.edges = defaultdict(list)
        self.weights = {}

    def add_nodes(self,nodes):
        for node in nodes:
            self.nodes.add(node)

    def add_edge(self,from_node, to_node, cost):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.weights[(from_node, to_node)] = cost

    def get_weight(self,n1,n2):
        key = (n1,n2) if (n1,n2) in self.weights.keys() else (n2,n1)
        return self.weights.get(key,"ERROR")

    def contains_edge(self,n1,n2):
        return (n1, n2) in self.weights.keys() or (n2,n1) in self.weights.keys()


def dijkstra(graph, start_node):

    Q = list(graph.nodes)
    Q.sort(key= lambda node: node.distance)

    start_node.distance = 0  # Distance from source to source

    while len(Q) > 0:
        current = Q.pop()
        for neighbor in graph.edges[current]:
            alt = current.distance + graph.get_weight(current,neighbor)
            if alt < neighbor.distance:
                neighbor.distance = alt
                neighbor.parent = current
                Q.sort(key=lambda node: node.distance)

    return graph.nodes



g = Graph()
number_of_nodes = 100
number_of_edges = number_of_nodes*3
n = [Node(x) for x in range(number_of_nodes)]
g.add_nodes(n)

for _ in range(number_of_edges):
    x = random.randint(0,number_of_nodes-1)
    y = random.randint(0,number_of_nodes-1)
    cost = random.randint(1,50)
    if not g.contains_edge(n[x],n[y]):
        g.add_edge(n[x], n[y], cost)

dijkstra(g,n[0])



# Draw graph
G = nx.Graph()
color_map = []
for node in n:
    G.add_node(node.id,distance=node.distance)
    if node.id == 0:
        color_map.append("blue")
    else:
        color_map.append("red")
for key in g.edges.keys():
    start = key
    ends = g.edges[key]
    for end in ends:
        G.add_edge(start.id,end.id,weight=g.get_weight(start,end))

pos = nx.spring_layout(G)
print(pos)

fig=plt.figure(1)
fig.set_size_inches(18.5, 10.5)
nx.draw(G,pos,node_color = color_map, with_labels=True, font_weight='bold',node_size=60,font_size=6)
nx.draw_networkx_edge_labels(G, pos,font_size=5)
plt.show()





