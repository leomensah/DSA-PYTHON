class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
"""
ITERATIVE SOLUTION
"""
class Solution:
    def reverseList(self, head: Node) -> Node:
        prev, curr = None, head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
"""
RECURSIVE SOLUTION
"""

class Solution:
    def reverseList(self, head: Node) -> Node:
        def recursive(head, previous):
            if not head:
                return previous
            result = recursive(head.next, head)
            head.next = previous
            return result
        return recursive(head, None)

input = [1,2,3,4,5]
ouput = [5,4,3,2,1]