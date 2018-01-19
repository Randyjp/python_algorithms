# 4.10) Given two trees t1 and t2, find if t2 is a subtree of t1

from collections import deque
from trees_and_graphs.minimal_tree import create_binary_search


def sub_tree(node1, node2):
    if node1 is None or node2 is None:
        return False
    visited_nodes = {}
    return bfs(node1, node2, visited_nodes)


def bfs(node1, node2, visited_nodes):
    queue = deque()
    visited_nodes[node1] = True
    queue.append(node1)

    while len(queue) > 0:
        node = queue.popleft()
        if check_if_equal(node, node2):
            return True

        for child in node.get_children():
            if not visited_nodes.get(child, False):
                visited_nodes[child] = True
                queue.append(child)
    return False


def traverse(node, node_list):
    if node is None:
        return
    traverse(node.left, node_list)
    node_list.append(str(node.data))
    traverse(node.right, node_list)


def check_if_equal(node1, node2):
    if node1.data != node2.data:
        return False

    list_n1 = []
    list_n2 = []
    traverse(node1, list_n1)
    traverse(node2, list_n2)
    str1 = ''.join(list_n1)
    str2 = ''.join(list_n2)

    if str2 in str1:
        return True
    return False


# test code
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tree1 = create_binary_search(numbers)
tree2 = create_binary_search([2, 3, 4])

print(sub_tree(tree1, tree2))
