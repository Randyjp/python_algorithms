from graph import Node, Graph
from collections import deque


# 4.1) given a directed graph, find if here is a path between two nodes

def search(graph, node1, node2):
    if node1 == node2:  # if they are the same return
        return True
    # mark all nodes of graph as visited
    for node in graph.nodes:
        node.visited = False

    queue = deque()
    node1.visited = True  # mark your root node as already visited
    queue.append(node1)

    while len(queue) > 0:
        new_node = queue.popleft()
        # you could visit the node here and do something --> visit(node)
        for n in new_node.get_adjacent():
            # mark adjacent nodes as visited then append them to the queue
            # this will ensure they are visited on the next 'level'
            if not n.visited:
                n.visited = True
                queue.append(n)
            if n == node2:
                return True
    return False


# test code
three = Node(3)
zero = Node(0)
one = Node(2)
two = Node(1)

three.children = [two]
zero.children = [one]
one.children = [two]
two.children = [three]

grafo = Graph([zero, one, two, three])

print(search(grafo, three, one))
