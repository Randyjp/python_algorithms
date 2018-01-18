# 4.2) Given a sorted array with unique integers,  create a binary tree with minimal height

class TreeNode:
    __slots__ = 'data', 'right', 'left'

    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


def create_binary_search(arr):
    size = len(arr)

    if size < 1:
        return
    if size == 1:
        return TreeNode(arr[0])

    mid_point = int(size / 2)
    node = TreeNode(arr[mid_point])

    if len(arr[0:mid_point]) > 0:
        left_node = create_binary_search(arr[0:mid_point])
        node.left = left_node
    if len(arr[mid_point+1:size]) > 0:
        right_node = create_binary_search(arr[mid_point+1:size])
        node.right = right_node

    return node

# test code
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# tree = create_binary_search(numbers)
# print(tree)

