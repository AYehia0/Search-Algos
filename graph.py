# Using defaultdict to avoid keyErrors, since it provids default value for 404 keys
from collections import defaultdict

class GraphTree:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_node(self, node, edge):
        self.graph[node].append(edge)

    def print_graph(self):
        print(self.graph)


