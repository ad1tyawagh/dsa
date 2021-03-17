class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next


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
print_list(head)
