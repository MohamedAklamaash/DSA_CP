
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def reverse(self):
        current = self.head
        if not current:  # Empty list
            return

        while current:
            # Swap the next and prev pointers
            current.next, current.prev = current.prev, current.next

            # Move to the next node (which is the previous node before the swap)
            current = current.prev

        # Update head to the new front of the list (the last node before reversal)
        if current:
            self.head = current.prev

dll = DoublyLinkedList()
dll.append(10)
dll.append(20)
dll.append(30)
dll.append(40)

print("Original List:")
dll.traverse()

dll.reverse()
print("\nReversed List:")
dll.traverse()
