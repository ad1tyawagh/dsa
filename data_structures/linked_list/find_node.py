from sys import stdin

# Following is the Node class already written for the Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def findNode(head, n):
    # Your code goes here
    if head == None:
        return -1
    curr = head
    position = 0
    while curr is not None:
        if curr.data == n:
            return position
        curr = curr.next
        position = position + 1

    return -1


# Taking Input Using Fast I/O


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
    print(findNode(head, n))

    num_testcases -= 1
