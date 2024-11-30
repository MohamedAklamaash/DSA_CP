
def count_inversions(arr):
    def merge_sort_and_count(arr):
        if len(arr) <= 1:
            return arr, 0

        mid = len(arr) // 2
        left, left_inv = merge_sort_and_count(arr[:mid])
        right, right_inv = merge_sort_and_count(arr[mid:])
        
        merged, merge_inv = merge_and_count(left, right)
        return merged, left_inv + right_inv + merge_inv

    def merge_and_count(left, right):
        merged = []
        i = j = inversions = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                inversions += len(left) - i  # Count inversions

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, inversions

    _, total_inversions = merge_sort_and_count(arr)
    return total_inversions

# Example usage
arr = [2, 4, 1, 3, 5]
print("Number of inversions:", count_inversions(arr))

