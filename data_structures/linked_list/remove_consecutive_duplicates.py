from sys import stdin

# Following is the Node class already written for the Linked List
class Node:
    def __init__(self, list_of_data):
        self.list_of_data = list_of_data
        self.next = None


def remove_duplicates(head):

    # empty list
    if head == None or head.next == None:
        return head

    # traverse the list
    temp1 = head
    temp2 = head.next

    while temp2 is not None:
        if temp1.list_of_data == temp2.list_of_data:
            while temp2 is not None and temp1.list_of_data == temp2.list_of_data:
                temp = temp2
                temp2 = temp2.next
            temp1.next = temp2
            temp.next = None
        else:
            temp1 = temp1.next
            temp2 = temp2.next

    return head


# Taking Input Using Fast I/O
def take_input():
    
    head = None
    tail = None

    list_of_data = list(map(int, stdin.readline().rstrip().split(" ")))

    count = 0
    while (count < len(list_of_data)) and (list_of_data[count] != -1):
        data = list_of_data[count]
        new_node = Node(data)

        if head is None:
            head = new_node
            tail = new_node

        else:
            tail.next = new_node
            tail = new_node

        count += 1

    return head


def print_linked_list(head):

    while head is not None:
        print(head.list_of_data, end=" ")
        head = head.next

    print()


# main
num_testcases = int(stdin.readline().strip())

while num_testcases > 0:
    head = take_input()

    head = remove_duplicates(head)
    print_linked_list(head)

    num_testcases -= 1
