from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length_of_list(head):
    current_node = head
    length_of_list = 0
    while current_node is not None:
        length_of_list += 1
        current_node = current_node.next

    return length_of_list


def append_last_n_to_first(head, n):
    # Your code goes here
    if n >= length_of_list(head) or n == 0:
        return head
    req_pos = length_of_list(head) - n - 1
    current_node = head
    while req_pos > 0:
        current_node = current_node.next
        req_pos -= 1

    last_n = current_node.next
    current_node.next = None
    temp = last_n
    while temp.next is not None:
        temp = temp.next
    temp.next = head
    return last_n


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
num_testcases = int(stdin.readline().rstrip())

while num_testcases > 0:

    head = take_input()
    n = int(stdin.readline().rstrip())

    head = append_last_n_to_first(head, n)
    print_linked_list(head)

    num_testcases -= 1
