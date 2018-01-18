# 4.4) check if binary tree is balanced

from trees_and_graphs.minimal_tree import TreeNode
from trees_and_graphs.minimal_tree import create_binary_search


def check_height(node):
    if node is None:
        return 0
    # check if left branch is balanced
    left_height = check_height(node.left)
    if left_height == -1:
        return -1

    # check if right branch is balanced
    right_height = check_height(node.right)
    if right_height == -1:
        return -1

    # if both are, check current node
    if abs(left_height - right_height) > 1:
        return -1
    else:
        return max(left_height, right_height) + 1


def is_balanced(node):
    height = check_height(node)
    return height > -1


# test code
# tree = TreeNode(1)
# tree1 = TreeNode(2)
# tree2 = TreeNode(1)
# tree3 = TreeNode(1)
# tree4 = TreeNode(1)
# tree5 = TreeNode(1)
# tree6 = TreeNode(10)
# tree7 = TreeNode(10)
#
# tree.left = tree2
# tree.right = tree3
# tree3.right = tree5
# tree5.right = tree4
# tree4.right = tree6
# tree6.right = tree7
# test code
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tree = create_binary_search(numbers)

res = is_balanced(tree)
print(res)
