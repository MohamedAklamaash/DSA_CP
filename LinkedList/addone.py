
class Solution:
    def addOneUtil(self, head):
        # Base case: if the current node is None, return carry 1
        if not head:
            return 1  # Return carry

        # Recursively add one to the rest of the list
        carry = self.addOneUtil(head.next)

        # After recursion, process the current node
        new_value = head.data + carry
        head.data = new_value % 10  # Update the current node data
        carry = new_value // 10  # Update carry (either 0 or 1)

        # If there is a carry left after processing the current node, return carry to propagate
        return carry

    def addOne(self, head):
        # Step 1: Recursively add one to the linked list
        carry = self.addOneUtil(head)

        # Step 2: If carry is 1, it means we need to insert a new node at the front
        if carry:
            new_node = Node(carry)  # Create new node with value = 1
            new_node.next = head  # Link it to the original head
            head = new_node  # Update head to the new node

        return head

