class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        noofzeros = 0
        maxi = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                noofzeros += 1
            
            while noofzeros > k:
                if nums[l] == 0:
                    noofzeros -= 1
                l += 1
            
            maxi = max(maxi, r - l + 1)
        
        return maxi

