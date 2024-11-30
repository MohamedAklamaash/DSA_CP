
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        max_product = nums[0]  # Tracks the max product ending at the current position
        min_product = nums[0]  # Tracks the min product ending at the current position
        global_max = nums[0]   # Tracks the overall max product

        for i in range(1, len(nums)):
            num = nums[i]
            if num < 0:  # Swap max and min if the current number is negative
                max_product, min_product = min_product, max_product

            max_product = max(num, max_product * num)  # Max of starting new subarray or extending
            min_product = min(num, min_product * num)  # Min of starting new subarray or extending

            global_max = max(global_max, max_product)  # Update the global maximum

        return global_max

