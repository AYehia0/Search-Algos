from graph import GraphTree

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'B'],
    'D' : [],
    'E' : ['F', 'C'],
    'F' : []
}

g = GraphTree()
g.add_node('A', 'B')
g.add_node('A', 'C')
g.add_node('B', 'D')
g.add_node('B', 'E')
g.add_node('C', 'F')
g.add_node('C', 'B')
g.add_node('E', 'F')
g.add_node('E', 'C')

visited = set()
def dfs(visited, G, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in G[node]:
            dfs(visited, G, neighbor)

def test_dfs(visited, graph, node):
    # adding current node as visited 
    visited.add(node)

    # printing that node
    print(node, end="")

    # travelling the graph
    for neighbour in graph[node]:
        if neighbour not in visited:
            test_dfs(visited, graph, neighbour)




v = set()

#print(visited)
#print(len(graph))

dfs(visited, g.get_graph(), list(graph)[0])
test_dfs(v, g.get_graph(), 'A') 
