# Code : Merge Sort
# Send Feedback
# Sort a given linked list using Merge Sort.
# You don't need to print the elements, just sort the elements and return the head of updated LL.
# Input format :
# Linked list elements (separated by space and terminated by -1)
# Output format :
# Updated LL elements (separated by space)
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def midpoint(head):

    if head is None:
        return None

    slow = head
    fast = head

    while (fast.next is not None) and (fast.next.next is not None):
        slow = slow.next
        fast = fast.next.next

    return slow


def merge(head1, head2):

    temp = None

    if head1 is None:
        return head2
    if head2 is None:
        return head1

    if head1.data <= head2.data:
        temp = head1
        temp.next = merge(head1.next, head2)
        return temp
    else:
        temp = head2
        temp.next = merge(head2.next, head1)
        return temp


def mergeSort(head):

    if head is None or head.next is None:
        return head

    # get the middle point
    mid = midpoint(head)
    # store the head of right half
    next2mid = mid.next
    # point the left half's end to None
    mid.next = None

    # sort halves
    left = mergeSort(head)
    right = mergeSort(next2mid)

    # merge halves
    return merge(left, right)


def make_linked_list(arr):
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


# Main
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(" "))
# Create a Linked list after removing -1 from list
l = make_linked_list(arr[:-1])
l = mergeSort(l)
print_linked_list(l)
