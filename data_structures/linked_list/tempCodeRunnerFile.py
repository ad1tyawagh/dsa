
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


def appendLastNToFirst(head, n):
    # Your code goes here
    req_pos = length(head) - n - 1
    curr = head
    while req_pos > 0:
        curr = curr.next
        req_pos -= 1

    last_n = curr.next
    curr.next = None
    temp = last_n
    while temp.next is not None:
        temp = temp.next
    temp.next = last_n
    return last_n


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().rstrip())

while t > 0:

    head = takeInput()
    n = int(stdin.readline().rstrip())

    head = appendLastNToFirst(head, n)
    printLinkedList(head)

    t -= 1
