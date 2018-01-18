class Node:
    __slots__ = 'data', 'visited', 'children'

    def __init__(self, data):
        self.data = data
        self.visited = False
        self.children = []

    def get_adjacent(self):
        if len(self.children) < 1:
            return None
        return self.children


class Graph:
    def __init__(self, nodes):
        self.nodes = nodes
# test code
# three = Node(3)
# zero = Node(0)
# one = Node(2)
# two = Node(1)
#
# three.children = [two]
# zero.children = [one]
# one.children = [two]
# two.children = [three]
#
# grafo = Graph([zero, one, two, three])
#
# print(grafo)
