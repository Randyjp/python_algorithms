# 4.3) given a binary tree, create a linked list for each level

from Linked_Lists.SinglyLikedList import SinglyLikedList
from minimal_tree import create_binary_search


def list_depth(node):
    list_table = {}
    traverse(node, 0, list_table)
    return list_table


def traverse(node, level, list_table):
    if node is None:
        return
    traverse(node.left, level + 1, list_table)
    add_to_liked_list(node.data, level, list_table)
    traverse(node.right, level + 1, list_table)


def add_to_liked_list(data, level, list_table):
    temp_list = list_table.get(level, None)
    if temp_list is None:
        temp_list = SinglyLikedList()

    temp_list.add_element(data)
    list_table[level] = temp_list

# test code
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
node = create_binary_search(numbers)
lists = list_depth(node)
