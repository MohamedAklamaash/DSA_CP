def search_in_rotated_array_with_duplicates(arr, x):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is the target
        if arr[mid] == x:
            return mid

        # Handle duplicates: skip them
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        # Determine which half is sorted
        if arr[low] <= arr[mid]:  # Left half is sorted
            if arr[low] <= x < arr[mid]:  # Target in left half
                high = mid - 1
            else:  # Target in right half
                low = mid + 1
        else:  # Right half is sorted
            if arr[mid] < x <= arr[high]:  # Target in right half
                low = mid + 1
            else:  # Target in left half
                high = mid - 1

    return -1  # Target not found

# Example
arr = [2, 2, 2, 3, 4, 2]
x = 3
print(search_in_rotated_array_with_duplicates(arr, x))  # Output: 3

