
"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        oldToCopy = {None:None}

        curr = head
        while curr:
            node = Node(curr.val)
            oldToCopy[curr] = node
            curr = curr.next
        
        curr = head

        while curr:
            node = oldToCopy[curr]
            node.next = oldToCopy[curr.next]
            node.random = oldToCopy[curr.random]
            curr = curr.next
        return oldToCopy[head]

