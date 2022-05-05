class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Solution:
    def checkLinkedListPalindrome(self, head, tail):
        if not tail:
            return [head, True]
        # Recurse to the end of the linked list
        node = self.checkLinkedListPalindrome(head, tail.next)

        # Compare the head and the end of the linked list
        if (not node[0] or node[0].val != tail.val):
            return [None, False]
        return [node[0].next, True]


    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return False
        return self.checkLinkedListPalindrome(head, head)[1]
