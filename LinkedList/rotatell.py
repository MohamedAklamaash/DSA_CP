
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next:
            return head

        # Step 2: Calculate length and form a circular list
        curr = head
        n = 1
        while curr.next:
            curr = curr.next
            n += 1
        curr.next = head  # Form a circular list

        # Step 3: Compute effective rotations
        k = k % n
        if k == 0:
            curr.next = None  # Break the circular link
            return head

        # Step 4: Find the new tail
        steps_to_new_tail = n - k
        new_tail = head
        for _ in range(steps_to_new_tail - 1):
            new_tail = new_tail.next

        # Step 5: Set the new head and break the circle
        new_head = new_tail.next
        new_tail.next = None
        return new_head


