from sys import setrecursionlimit

setrecursionlimit(11000)


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Reverse a linked list recursively and return the head pointer
def reverse_recursive(head):

    # No need to do anything if list is empty or has a single element
    if head is None or head.next is None:
        return head

    # Reverse the rest of the list
    rest = reverse_recursive(head.next)

    # Put first element at the end
    head.next.next = head
    head.next = None

    # Fix the header pointer
    return rest


def generate_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


def print_linked_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()


# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(" "))

# Create a Linked list after removing -1 from list
l = generate_linked_list(arr[:-1])
l = reverse_recursive(l)
print_linked_list(l)
