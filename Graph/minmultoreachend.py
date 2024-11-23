from collections import deque

def minimumMultiplications(arr, start, end):
    """
    Find the minimum number of multiplications to transform 'start' to 'end' using elements from 'arr'.
    
    :param arr: List[int] - List of integers to multiply.
    :param start: int - Starting number.
    :param end: int - Target number.
    :return: int - Minimum multiplications, or -1 if not possible.
    """
    MOD = 10**5  # Limit the range of numbers
    visited = set()
    queue = deque([(start, 0)])  # (current number, steps)
    
    while queue:
        curr, steps = queue.popleft()
        
        # If we reach the end, return the steps
        if curr == end:
            return steps
        
        # Process all possible multiplications
        for num in arr:
            next_val = (curr * num) % MOD
            
            # If not visited, enqueue the next value
            if next_val not in visited:
                visited.add(next_val)
                queue.append((next_val, steps + 1))
    
    # If the queue is exhausted and end is not reached
    return -1

# Example Usage
arr = [2, 3]
start = 2
end = 12

print(minimumMultiplications(arr, start, end))  # Output: 2 (2 -> 4 -> 12)

