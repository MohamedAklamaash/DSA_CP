
def count_rotations(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is the pivot (minimum element)
        if arr[mid] < arr[high]:
            high = mid  # Minimum is in the left half
        elif arr[mid] > arr[high]:
            low = mid + 1  # Minimum is in the right half
        else:
            high -= 1  # Skip duplicates

    return low  # The index of the minimum element is the number of rotations

# Example
arr = [4, 5, 6, 7, 0, 1, 2]
print(count_rotations(arr))  # Output: 4


