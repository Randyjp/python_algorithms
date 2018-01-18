# 2.6) check if singly linked list is palindrome

from SinglyLikedList import SinglyLikedList


def is_palindrome(linked_list):
    node = linked_list.head
    temp_list = []

    while node is not None:
        temp_list.append(node.element)
        node = node.next

    return temp_list == temp_list[::-1]

# runner pointer solution

def is_palindrome_runner(linked_list):
    fast = slow = the_list.head
    stack = []

    while fast is not None and fast.next is not None:
        stack.append(slow.element)
        slow = slow.next
        fast = fast.next.next

    # deal with odd list
    if fast is not None:
        slow = slow.next

    while slow is not None:
        element = stack.pop()
        if slow.element != element:
            return False
        slow = slow.next
    return True

# test code

the_list = SinglyLikedList()
the_list.add_element(1)
the_list.add_element(2)
# the_list.add_element(5)
the_list.add_element(2)
the_list.add_element(1)

print(is_palindrome_runner(the_list))