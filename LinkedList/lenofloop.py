
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def countNodesInLoop(self, head):
        # Step 1: Detect the loop using Floyd’s Cycle Detection Algorithm
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next  # Move slow pointer by one
            fast = fast.next.next  # Move fast pointer by two

            # If slow and fast meet, a loop is detected
            if slow == fast:
                # Step 2: Calculate the length of the loop
                return self.countLoopLength(slow)
        
        return 0  # No loop found

    def countLoopLength(self, meeting_point):
        # Traverse the loop to calculate its length
        current = meeting_point
        count = 1
        while current.next != meeting_point:
            current = current.next
            count += 1
        return count

