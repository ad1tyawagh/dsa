# Bubble Sort (Iterative) LinkedList
# Send Feedback
# Sort a given linked list using Bubble Sort (iteratively). While sorting, you need to swap the entire nodes, not just the data.
# You don't need to print the elements, just sort the elements and return the head of updated LL.
# Input format : Linked list elements (separated by space and terminated by -1)`
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swap(n1, n2, p, n):
    pass


def bubbleSortLL(head):
    pass


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

# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(" "))

# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = bubbleSortLL(l)
printll(l)
