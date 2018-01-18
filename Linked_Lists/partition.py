# 2.4) Write code to partition a list around an x value

from SinglyLikedList import SinglyLikedList


# solution using lists/arrays
def partition(linked_list, x):
    current_node = linked_list.head
    greater_x = []
    smaller_x = []
    result = SinglyLikedList()

    while current_node is not None:
        if current_node.element <= x:
            smaller_x.append(current_node.element)
        else:
            greater_x.append(current_node.element)
        current_node = current_node.next

    smaller_x.sort()

    for e in (smaller_x + greater_x):
        result.add_element(e)

    return result


# test code

the_list = SinglyLikedList()
the_list.add_element(2)
the_list.add_element(9)
the_list.add_element(3)
the_list.add_element(5)
the_list.add_element(1)

new_list = partition(the_list, 3)
new_list.print_all()
