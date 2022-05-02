class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
        
def mergeTwoSortedLinkedList(NodeA, NodeB):
    if not (NodeA and NodeB):
        return NodeA or NodeB

    if NodeA.data < NodeB.data:
        NodeA.next = mergeTwoSortedLinkedList(NodeA.next, NodeB)
        return NodeA
    else:
        NodeB.next = mergeTwoSortedLinkedList(NodeA, NodeB.next)
        return NodeB
