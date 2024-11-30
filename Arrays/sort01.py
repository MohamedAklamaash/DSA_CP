
def sort01_with_steps(arr):
    left, right = 0, len(arr) - 1
    steps = 0

    while left < right:
        if arr[left] == 1 and arr[right] == 0:
            # Swap 1 at left with 0 at right
            arr[left], arr[right] = arr[right], arr[left]
            steps += 1
        if arr[left] == 0:
            left += 1
        if arr[right] == 1:
            right -= 1

    return arr, steps

# Example usage
arr = [1, 0, 1, 0, 1, 0]
sorted_arr, steps = sort01_with_steps(arr)
print(f"Sorted Array: {sorted_arr}, Steps: {steps}")

