# kReverse
# Send Feedback
# Implement kReverse( int k ) in a linked list i.e. you need to reverse first K elements then reverse next k elements and join the linked list and so on.
# Indexing starts from 0. If less than k elements left in the last, you need to reverse them as well. If k is greater than length of LL, reverse the complete LL.
# You don't need to print the elements, just return the head of updated LL.
# Input format :

# Line 1 : Linked list elements (separated by space and terminated by -1)


# Line 2 : k
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def kReverse(head, n):
    #  Implement kReverse( k ) in a linked list i.e. you need to reverse
    #  first K elements then reverse next k elements and join the linked list and
    #  so on. Indexing starts from 0. If less than k elements left in the last,
    #  you need to reverse them as well. If k is greater than length of LL,
    #  reverse the complete LL. If n is 4 and LL is:
    #  Input: 1 2 3 4 5 6 7 8 9 10
    #  Output: 4 3 2 1 8 7 6 5 10 9
    #############################
    # PLEASE ADD YOUR CODE HERE #
    #############################
    pass


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
i = int(input())
l = kReverse(l, i)
print_linked_list(l)
