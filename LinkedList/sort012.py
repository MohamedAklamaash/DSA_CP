
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head):
        # Count the occurrences of 0, 1, and 2
        count = [0, 0, 0]  # count[0] = count of 0's, count[1] = count of 1's, count[2] = count of 2's
        current = head
        
        while current:
            count[current.val] += 1
            current = current.next
        
        # Reconstruct the list based on the count
        current = head
        for value in range(3):
            while count[value] > 0:
                current.val = value
                count[value] -= 1
                current = current.next
        
        return head

