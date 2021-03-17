class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def reverseRecursive(head):

    if head is None or head.next is None:
        return head

    # Reverse the rest of the list
    rest = reverseRecursive(head.next)

    # Put first element at the end
    head.next.next = head
    head.next = None

    # Fix the header pointer
    return rest


def ll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def printll(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# Main
from sys import setrecursionlimit

setrecursionlimit(11000)
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(" "))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = reverseRecursive(l)
printll(l)
