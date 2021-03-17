from sys import stdin

# Following is the Node class already written for the Linked List


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def removeDuplicates(head):
    # Your code goes here
    # empty list
    if head == None or head.next == None:
        return head

    # traverse the list
    t1 = head
    t2 = head.next

    while t2 is not None:
        if t1.data == t2.data:
            while t2 is not None and t1.data == t2.data:
                temp = t2
                t2 = t2.next
            t1.next = t2
            temp.next = None
        else:
            t1 = t1.next
            t2 = t2.next

    return head


# Taking Input Using Fast I/O


def takeInput():
    head = None
    tail = None

    datas = list(map(int, stdin.readline().rstrip().split(" ")))

    i = 0
    while (i < len(datas)) and (datas[i] != -1):
        data = datas[i]
        newNode = Node(data)

        if head is None:
            head = newNode
            tail = newNode

        else:
            tail.next = newNode
            tail = newNode

        i += 1

    return head


# to print the linked list
def printLinkedList(head):

    while head is not None:
        print(head.data, end=" ")
        head = head.next

    print()


# main
t = int(stdin.readline().strip())

while t > 0:
    head = takeInput()

    head = removeDuplicates(head)
    printLinkedList(head)

    t -= 1
