# 4.8) Given two nodes in a binary search tree find their first common ancestor

from trees_and_graphs.minimal_tree import create_binary_search


def first_common_ancestor(root, node1, node2):
    if node1 == node2:
        return None
    ancestor = find_path(root, node1, node2)
    return ancestor.data if ancestor else None


def find_path(root, node1, node2):
    if root is None:
        return None
    found_right = find_path(root.right, node1, node2)
    found_left = find_path(root.left, node1, node2)

    # if (root == node1 or root == node2) and (found_left or found_right):
    #     return root
    if root == node1:
        return node1
    elif root == node2:
        return node2
    elif found_left and found_right:
        return root
    elif found_left:
        return found_left
    elif found_right:
        return found_right
    else:
        return None


# test code
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

tree = create_binary_search(numbers)
ancestor = first_common_ancestor(tree, tree.left, tree.right)
print(ancestor)
