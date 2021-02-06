from graph import GraphTree

g = GraphTree()
g.add_node('A', 'B')
g.add_node('A', 'C')
g.add_node('B', 'D')
g.add_node('B', 'E')
g.add_node('C', 'F')

def test_dfs(start, goal, level, visited_path, depth):
    # printing the current lvl
    print(f"Current level of search: {level}")
    print(f"Trying: {start}")

    # adding current node as visited
    visited_path.append(start)

    if start == goal:
        print('Goal was found!!')
        return visited_path

    if level == depth:
        return False

    print(f"Expanding the current node {start}")    
    # travelling the graph
    for neighbour in g.get_graph()[start]:
        if test_dfs(neighbour, goal, level+1, visited_path, depth):
            return visited_path
        else:
            #print("Goal wasn't found")
            visited_path.pop()
    return False

v = list()
ans = test_dfs('A', 'F', 0,v, 2)
print(ans)
