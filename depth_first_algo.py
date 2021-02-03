graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F', 'B'],
    'D' : [],
    'E' : ['F', 'C'],
    'F' : []
}


visited = set()
def dfs(visited, G, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in G[node]:
            dfs(visited, G, neighbor)

#print(visited)
#print(len(graph))

dfs(visited, graph, list(graph)[0])

