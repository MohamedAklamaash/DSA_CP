class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def remove_duplicates_from_dll(head):
    if not head:
        return head

    curr = head
    while curr and curr.next:
        # If duplicate, skip the next node
        if curr.val == curr.next.val:
            duplicate = curr.next
            curr.next = duplicate.next
            if duplicate.next:  # Update the `prev` pointer of the next node
                duplicate.next.prev = curr
        else:
            curr = curr.next

    return head

