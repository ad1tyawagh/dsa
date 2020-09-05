class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def length(head):

    length = 0
    curr = head

    while curr.next is not None:
        length += 1

    return length


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next


def insert(head, data, i):
    #  Insert at ith position
    if i < 0 or i > length(head):
        return
    curr = head
    new_node = Node(data)
    while i > 0:
        curr = curr.next
        i -= 1
    nxt = curr.next
    curr.next = new_node
    new_node.next = nxt


def make_list():

    lst = [int(x) for x in input().split()]
    head = None
    last = head
    for item in lst:

        new_node = Node(item)
        if head == None:
            head = new_node
            last = new_node
        else:
            last.next = new_node
            last = new_node

    return head


head = make_list()
insert(head, 10, 0)
print_list(head)
