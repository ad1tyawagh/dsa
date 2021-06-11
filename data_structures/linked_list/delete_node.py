from sys import stdin

# Following is the Node class already written for the Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    curr = head
    length = 0
    while curr is not None:
        length += 1
        curr = curr.next

    return length


def deleteNode(head, pos):
    # If linked list is empty
    if head == None:
        return

    # Store head node
    temp = head

    # If head needs to be removed
    if pos == 0:
        head = temp.next
        temp = None
        return head

    # Find previous node of the node to be deleted
    for i in range(pos - 1):
        temp = temp.next
        if temp is None:
            break

    # If position is more than number of nodes
    if temp is None:
        return head
    if temp.next is None:
        return head

    # Node temp.next is the node to be deleted
    # store pointer to the next of node to be deleted
    next = temp.next.next

    # Unlink the node from linked list
    temp.next = None

    temp.next = next
    return head


def take_input():
    head = None
    tail = None

    list_of_data = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(list_of_data)) and (list_of_data[i] != -1):
        data = list_of_data[i]
        new_node = Node(data)

        if head is None:
            head = new_node
            tail = new_node

        else:
            tail.next = new_node
            tail = new_node

        i += 1

    return head


# to print the linked list
def print_linked_list(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
num_testcases = int(stdin.readline().strip())

while num_testcases > 0:

    head = take_input()
    pos = int(stdin.readline().rstrip())

    head = deleteNode(head, pos)
    print_linked_list(head)

    num_testcases -= 1
