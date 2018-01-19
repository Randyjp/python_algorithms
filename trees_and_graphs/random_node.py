# 4.11) create a binary tree class tha supports, insert, delete, find and get random node
from random import randint


class TreeNode:
    __slots__ = 'data', 'right', 'left', 'size'

    def __init__(self, data):
        self.data = data
        self.size = 1
        self.right = None
        self.left = None

    def get_children(self):
        if self.right and self.left:
            return [self.left, self.right]
        elif self.right:
            return [self.right]
        elif self.left:
            return [self.left]
        return []

    def find(self, value):
        if self is None:
            return
        found_left = self.left.find(value) if self.left else None
        if self.data == value:
            return self
        found_right = self.right.find(value) if self.right else None

        if found_right:
            return found_right
        if found_left:
            return found_left
        return None

    def insert(self, value):
        if value > self.data:
            if self.right:
                self.right.insert(value)
            else:
                self.right = TreeNode(value)
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = TreeNode(value)
        self.size += 1

    def delete(self, value):
        # TODO : properly update the size of tree
        # find node to delete
        node = self.find(value)
        if node is None:
            # there's nothing to delete, return False
            return False
        # check if node has 2 children
        if node.left and node.right:
            # if yes, find the rightmost node of the left sub-tree
            parent_node = node
            replacement = node.left
            while replacement.right:
                parent_node = replacement
                replacement = replacement.right
            node.data = replacement.data
            parent_node.right = None
            node.size -= 1
            return True

            # cases for one child
        if node.left:
            node.data = node.left.data
            node.left = None
            node.size -= 1
            return True
        if node.right:
            node.data = node.right.data
            node.right = None
            node.size -= 1
            return True
        return False

    def random_node(self):
        rand = randint(1, self.size)
        if rand < (self.left.size if self.left else 0):
            return self.left.random_node()
        if rand == self.size:
            return self.data
        else:
            return self.right.random_node() if self.right else self


# test code

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 200, 210, 315, 500, 250]

tree = TreeNode(100)

for num in numbers:
    tree.insert(num)

tree.delete(315)
print(tree.random_node())
