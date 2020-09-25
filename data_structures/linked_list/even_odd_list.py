# Even after Odd LinkedList
# Send Feedback
# Arrange elements in a given Linked List such that, all even numbers are placed after odd numbers. Respective order of elements should remain same.
# Note: Input and Output has already managed for you. You don't need to print the elements, instead return the head of updated LL.
# Input format:
# Linked list elements (separated by space and terminated by -1)
# Output format:
# Print the elements of updated Linked list.
# Problem ID 331 even after odd in a LL
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def arrange_LinkedList(head):

    odd = []
    even = []

    while head is not None:
        if head.data % 2 == 0:
            even.append(head.data)
        else:
            odd.append(head.data)
        head = head.next

    head = None
    tail = None

    for num in odd:
        node = Node(num)
        if head is None:
            head = node
            tail = head
        else:
            tail.next = node
            tail = tail.next
    for num in even:
        node = Node(num)
        tail.next = node
        tail = tail.next

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
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(' '))
# Create a Linked list after removing -1 from list
l = ll(arr[:-1])
l = arrange_LinkedList(l)
printll(l)
