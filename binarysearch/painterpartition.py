
def canAllocate(arr, n, k, maxPages):
    workers = 1  # Start with one worker
    pagesAssigned = 0  # Pages assigned to the current worker
    
    for i in range(n):
        # If assigning the current book exceeds the maxPages
        if pagesAssigned + arr[i] > maxPages:
            workers += 1  # Assign a new worker
            pagesAssigned = arr[i]  # Start with the current book for the new worker
            if workers > k:  # If we need more than k workers, it's not feasible
                return False
        else:
            pagesAssigned += arr[i]  # Assign the book to the current worker

    return True

def painterPartition(arr, n, k):
    # Binary search range for the maximum pages a worker can handle
    low = max(arr)  # Minimum possible "max pages" for any worker
    high = sum(arr)  # Maximum possible "max pages" (if one worker does everything)
    
    ans = -1
    while low <= high:
        mid = (low + high) // 2  # Midpoint is the candidate max pages a worker can handle
        if canAllocate(arr, n, k, mid):
            ans = mid  # If we can allocate, try for a lower max pages
            high = mid - 1
        else:
            low = mid + 1  # Otherwise, increase the max pages

    return ans

# Example Usage:
arr = [10, 20, 30, 40]  # Books with pages
n = len(arr)  # Number of books
k = 2  # Number of workers/painters

ans = painterPartition(arr, n, k)
print("The minimum maximum pages a painter has to paint:", ans)

