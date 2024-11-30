
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        curr = head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        
        prev = None
        curr = head

        for _ in range(k):
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        
        head.next = self.reverseKGroup(curr,k)
        return prev

