
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
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

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def delete_by_value(self, value):
        current = self.head
        if not current:
            return "List is empty"
        if current.data == value:
            self.head = current.next
            return
        prev = None
        while current and current.data != value:
            prev = current
            current = current.next
        if not current:
            return "Value not found"
        prev.next = current.next

    def delete_nth_node(self, position):
        if position < 0:
            return "Invalid position"
        current = self.head
        if not current:
            return "List is empty"
        if position == 0:
            self.head = current.next
            return
        prev = None
        count = 0
        while current and count < position:
            prev = current
            current = current.next
            count += 1
        if not current:
            return "Position out of bounds"
        prev.next = current.next

    def insert_after_nth_node(self, position, data):
        current = self.head
        count = 0
        while current and count < position:
            current = current.next
            count += 1
        if not current:
            return "Position out of bounds"
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    def update_nth_node(self, position, new_data):
        current = self.head
        count = 0
        while current and count < position:
            current = current.next
            count += 1
        if not current:
            return "Position out of bounds"
        current.data = new_data

ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Initial List:")
ll.traverse()

# Deletion by value
ll.delete_by_value(20)
print("\nAfter deleting 20:")
ll.traverse()

# Deletion of nth node
ll.delete_nth_node(1)
print("\nAfter deleting node at position 1:")
ll.traverse()

# Insertion after nth node
ll.insert_after_nth_node(0, 25)
print("\nAfter inserting 25 after position 0:")
ll.traverse()

# Update nth node
ll.update_nth_node(1, 35)
print("\nAfter updating position 1 to 35:")
ll.traverse()
