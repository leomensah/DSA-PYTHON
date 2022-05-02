def removeLinkedList(head, val):
    if head is None:
        return head
    head.next = removeLinkedList(head.next, val)

    if head.val != val:
        return head
    else:
        return head.next