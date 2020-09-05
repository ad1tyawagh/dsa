from sys import setrecursionlimit


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):
    length = 0
    while head is not None:
        head = head.next
        length += 1
    return length


def deleteRec(head, pos):
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
        return  head
    if temp.next is None:
        return head

    # Node temp.next is the node to be deleted
    # store pointer to the next of node to be deleted
    next = temp.next.next

    # Unlink the node from linked list
    temp.next = None

    temp.next = next
    return head


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
        print(head.data, end=' ')
        head = head.next
    print()


# Main
setrecursionlimit(11000)
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
i = int(input())
l = deleteRec(l, i)
printll(l)
