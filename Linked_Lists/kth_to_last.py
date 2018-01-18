# find the kth to last element on a singly liked list

from SinglyLikedList import SinglyLikedList


# Solution if you know the size of the list

def kth_to_last_size(linked_list, size, k):
    current_node = linked_list.head
    # size = linked_list.size # uncomment and remove the size from param for knowing size answer
    count = 1

    if k > size:
        return False

    while count < (size - k) and current_node is not None:
        current_node = current_node.next
        count += 1

    return current_node.element


# solution with size unknown

def kth_to_last_no_size(linked_list, k):
    size = get_list_size(linked_list)
    return kth_to_last_size(linked_list, size,k)


def get_list_size(linked_list):
    current_node = linked_list.head
    size = 0

    while current_node is not None:
        size += 1
        current_node = current_node.next

    return size


# test code

the_list = SinglyLikedList()
the_list.add_element(2)
the_list.add_element(9)
the_list.add_element(3)
the_list.add_element(5)
the_list.add_element(1)

the_list.print_all()
print("Found: ", kth_to_last_no_size(the_list, 2))
