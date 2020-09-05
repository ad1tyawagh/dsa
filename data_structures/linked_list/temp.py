def length(head):
    curr = head
    length = 0
    while curr is not None:
        length += 1
        curr = curr.next

    return length