from graph import GraphTree

"""

The ago works by visiting all nodes and adding node's children to a queue , then removing the head of the queue and visiting it's childrens and so on until the queue is empty

"""

def bfs(tree, start):

    # to keep track of visited nodes
    visited = []
    
    # adding the head to the queue
    queue = list()

    queue.append(start)

    # travelling the tree, till the queue is empty
    while queue:
        # dequeue , then visit its childrens and mark as visited
        # remove the first element of the list
        start = queue.pop(0)
        print(start, end=' ')
        if start not in visited:
            visited.append(start)
            nodes_children = tree[start]

            for child in nodes_children:
                queue.append(child)
    return visited

g = GraphTree()

g.add_node(0, 1)
g.add_node(0, 2)
g.add_node(1, 3)
g.add_node(1, 4)
g.add_node(1, 5)
g.add_node(5, 7)
g.add_node(5, 8)
g.add_node(2, 6)


bfs(g.get_graph(), 7)
