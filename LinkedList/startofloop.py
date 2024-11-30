
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Step 1: Detect if a loop exists using Floyd’s Cycle Detection Algorithm
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # If slow and fast meet, a loop is detected
            if slow == fast:
                break
        else:
            # If no loop is found, return None
            return None

        # Step 2: Find the starting point of the loop
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # This is the starting node of the loop

