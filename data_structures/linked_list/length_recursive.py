from sys import setrecursionlimit


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def lengthRecursive(head):

    if head == None:
        return 0
    length = 0
    temp = head.next
    length = lengthRecursive(temp) + 1
    return length


def make_linked_list(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    last = head
    for data in arr[1:]:
        last.next = Node(data)
        last = last.next
    return head


# Main
setrecursionlimit(11000)
# Read the link list elements including -1
arr = list(int(i) for i in input().strip().split(" "))
# Create a Linked list after removing -1 from list
l = make_linked_list(arr[:-1])
len = lengthRecursive(l)
print(len)
