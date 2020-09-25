class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def swap_nodes(head, i, j):

    if head == None or head.next == None:
        return head

    if i > j:
        i, j = j, i

    a_prev = None
    a = head
    c_a = 0

    while c_a < i:
        if a_prev == None:
            a_prev = head
            a = a.next
        else:
            a_prev = a_prev.next
            a = a.next
        c_a += 1

    a_next = a.next

    b_prev = None
    b = head
    c_b = 0

    while c_b < j:
        if b_prev == None:
            b_prev = head
            b = b.next
        else:
            b_prev = b_prev.next
            b = b.next
        c_b += 1

    b_next = b.next

    if a_prev = None:
        
    else:
        a_prev.next = b
        b.next = a_next
        a.next = b_next
        b_prev.next = a

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
i, j = list(int(i) for i in input().strip().split(' '))
l = swap_nodes(l, i, j)
printll(l)
