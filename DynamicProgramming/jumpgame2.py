
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [-1] * n  

        def f(ind):
            if ind >= n - 1:  # Reached or exceeded the destination
                return 0
            if dp[ind] != -1: 
                return dp[ind]

            min_jumps = float('inf')
            for step in range(1, nums[ind] + 1):
                min_jumps = min(min_jumps, 1 + f(ind +step ))
            
            dp[ind] = min_jumps
            return dp[ind]

        return f(0)


