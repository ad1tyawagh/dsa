class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None


def make_list():

    lst = [int(x) for x in input("Enter the list: ").split()]
    head = None

    for item in lst:
        new_node = Node(item)
        if head is None:
            head = new_node
        else:
            curr = head
            while curr.next is not None:
                curr = curr.next
            curr.next = new_node
    return head


head = make_list()
