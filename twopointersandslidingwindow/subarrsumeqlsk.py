class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefixsum = {0:1}
        curr_sum = 0
        res = 0
        for num in nums:
            curr_sum+=num

            if curr_sum -k in prefixsum:
               res += prefixsum[curr_sum-k]
            if curr_sum in prefixsum:
                prefixsum[curr_sum] += 1 
            else:
                prefixsum[curr_sum] =1
        return res
