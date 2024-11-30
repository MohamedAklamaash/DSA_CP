
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        def getlen(head):
            curr = head
            n = 0

            while curr:
                curr = curr.next
                n+=1
            return n
        
        lenA = getlen(headA)
        lenB = getlen(headB)

        if lenA > lenB:

            for _ in range(lenA - lenB):
                headA = headA.next
        elif lenB > lenA:

            for _ in range(lenB - lenA):
                headB = headB.next
        
        while headA and headB:

            if headA == headB:
                return headA
            
            headA = headA.next
            headB = headB.next
        return None
