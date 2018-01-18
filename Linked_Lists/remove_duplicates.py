# Write code to remove duplicates

from SinglyLikedList import SinglyLikedList


# solution with hash table

def delete_duplicates_hash(l1):
    current_node = l1.head
    previous_node = None
    frequencies = {}

    while current_node is not None:
        if frequencies.get(current_node.element, 0) > 0:
            delete_node(current_node, previous_node)
        else:
            frequencies[current_node.element] = 1 + frequencies.get(current_node.element, 0)

        previous_node = current_node
        current_node = current_node.next


# solution with two pointers
def delete_duplicates_runner(l1):
    current_node = l1.head
    runner = l1.head.next.next
    previous_node = None

    while current_node is not None:
        while runner is not None:
            if current_node.element == runner.element:
                delete_node(current_node, previous_node)
            previous_node = runner
            runner = runner.next
        current_node = current_node.next

# list solution

def delete_duplicates_list(l1):
    current_node = l1.head
    previous_node = None
    node_buffer = []

    while current_node is not None:
        if current_node.element in node_buffer:
            delete_node(current_node, previous_node)
        else:
            node_buffer.append(current_node.element)
        previous_node = current_node
        current_node = current_node.next

def delete_node(node, previous):
    previous.next = node.next


# create list

the_list = SinglyLikedList()
the_list.add_element(2)
the_list.add_element(5)
the_list.add_element(3)
the_list.add_element(5)
the_list.add_element(1)

delete_duplicates_list(the_list)
the_list.print_all()
