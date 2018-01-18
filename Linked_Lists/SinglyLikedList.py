from Linked_Lists.Node import Node


class SinglyLikedList:

    def __init__(self):
        self.size = 0
        self.head = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def add_element(self, element):
        d = Node(element, self.head)
        self.head = d
        self.size += 1

    def add_node(self, node):
        self.head = node
        self.size += 1

    def remove_element(self):
        # TODO: throw exception
        if self.is_empty():
            return False
        self.head = self.head.next
        self.head.next = None
        self.size -= 1

    def print_all(self):
        node = self.head
        while node is not None:
            print(node.element)
            node = node.next


# Test list
# l = SinglyLikedList()
# l.add_element(1)
# l.add_element(2)
# l.add_element(3)
# l.add_element(4)
# l.add_element(5)
#
# l.print_all()
