# 2.5)

from SinglyLikedList import SinglyLikedList


def add_lists(l1, l2):
    added = get_real_number(l1) + get_real_number(l2)
    return turn_into_list(added)


def get_real_number(linked_list):
    node = linked_list.head
    factor = 1
    result = 0

    while node is not None:
        element = node.element
        result += element * factor
        factor *= 10
        node = node.next
    return result

# recursive solution
# def add_list_recursive(l1, l2, carry):
#     if l1 is None and l2 is None and carry == 0:
#         return None
#
#     result = SinglyLikedList().head
#     value = carry
#
#     if l1 is not None:
#         value += l1.element
#     if l2 is not None:
#         value += l2.element
#
#     result.add_element(value % 10)
#
#     # recurse
#
#     if l1 is not None or l2 is not None:
#         more = add_list_recursive(None if l1 is None else l1.next,
#                                   None if l2 is None else l2.next,
#                                   1 if value >= 10 else 0)
#         result.add_element(None if more is None else more.head.element)
#     return result

def turn_into_list(number):
    digits = [int(i) for i in str(number)]
    new_list = SinglyLikedList()

    for digit in digits[::-1]:
        new_list.add_element(digit)
    return new_list


# test code
list1 = SinglyLikedList()
list1.add_element(2)
list1.add_element(2)
list1.add_element(0)

list2 = SinglyLikedList()
list2.add_element(1)
list2.add_element(1)
list2.add_element(0)

result = add_lists(list1, list2)
result.print_all()
