
def count_reverse_pairs(nums):
    def merge_sort_and_count(nums):
        if len(nums) <= 1:
            return nums, 0

        mid = len(nums) // 2
        left, left_count = merge_sort_and_count(nums[:mid])
        right, right_count = merge_sort_and_count(nums[mid:])

        merged, cross_count = merge_and_count(left, right)
        return merged, left_count + right_count + cross_count

    def merge_and_count(left, right):
        i = j = 0
        merged = []
        count = 0

        # Count reverse pairs
        for num in left:
            while j < len(right) and num > 2 * right[j]:
                j += 1
            count += j

        # Merge step
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged, count

    _, total_count = merge_sort_and_count(nums)
    return total_count

# Example usage
nums = [1, 3, 2, 3, 1]
print("Number of reverse pairs:", count_reverse_pairs(nums))

