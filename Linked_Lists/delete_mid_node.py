# 2.3) Delete node in the middle of a singly linked list given access only to that node

from SinglyLikedList import SinglyLikedList


def delete_node(node):
    if node is None:
        return
    next_node = node.next
    # if our node is the last node on the list, just replace all its content with null
    if next_node is None:
        node.element = None
        node.next = None
    # else 'fake' a deletion by replacing our current node's value with the next node
    else:
        node.element = next_node.element
        node.next = next_node.next
        next_node = None


# test code

the_list = SinglyLikedList()
the_list.add_element(2)
the_list.add_element(9)
the_list.add_element(3)
the_list.add_element(5)
the_list.add_element(1)

the_list.print_all()
delete_node(the_list.head)
print('===================')
the_list.print_all()
