# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = [head]
        current = head.next
        while current:
            nodes.append(current)
            current = current.next
        mid = len(nodes) // 2
        return nodes[mid]

