class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, val):
        self.stack1.append(val)

    def dequeue(self):
        if not self.stack2:  # Transfer elements from stack1 to stack2 if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()

    def front(self):
        if not self.stack2:  # Transfer elements from stack1 to stack2 if stack2 is empty
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]


if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    
    q = int(data[0])  # Number of queries
    queue = Queue()
    
    results = []
    for i in range(1, q + 1):
        query = data[i].split()
        query_type = int(query[0])
        
        if query_type == 1:  # Enqueue operation
            value = int(query[1])
            queue.enqueue(value)
        elif query_type == 2:  # Dequeue operation
            queue.dequeue()
        elif query_type == 3:  # Print front element
            results.append(queue.front())
    
    # Print all results for "3" queries
    for result in results:
        print(result)

