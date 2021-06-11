from sys import setrecursionlimit, stdin

setrecursionlimit(10 ** 6)


# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def printReverse(head):
    # Your code goes here
    if head is None:
        return
    if head.next is None:
        print(head.data, end=" ")
        return

    printReverse(head.next)
    print(head.data, end=" ")
    return


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
    printReverse(head)
    print()

    num_testcases -= 1
