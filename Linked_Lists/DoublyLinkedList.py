class _Node:
    __slots__ = 'element', 'next', 'prev'

    def __init__(self, element, next, prev):
        self.element = element
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        # create sentinel Nodes
        self.head = _Node(None, None, None)
        self.tail = _Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.head.next

    def last(self):
        if self.is_empty():
            raise Exception("Empty list")
        return self.tail.prev

    def _add_in_between(self, element, prev_node, next_node):
        if not prev_node.next == next_node:
            raise Exception("Add in between proper nodes")

        newest = _Node(element, next_node, prev_node)
        prev_node.next = newest
        # newest.prev = prev_node
        next_node.prev = newest
        self.size += 1
        return newest

    def delete_node(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

        node.prev = None
        node.next = None
        self.size -= 1

        return node.element

    def add_first(self, element):
        old_first = self.head.next
        return self._add_in_between(element, self.head, old_first)

    def add_last(self, element):
        old_last = self.tail.prev
        return self._add_in_between(element, old_last, self.tail)

    def print_all(self):
        node = self.head
        while node.next is not None:
            print(node.element)
            node = node.next
        print(node.element)

# testing the code
# d_list = DoublyLinkedList()
# d_list.add_first(2)
# d_list.add_first(3)
# d_list.add_last(10)
# node_to_delete = d_list.add_first(9)
# # d_list.delete_node(node_to_delete)
#
# d_list.print_all()

