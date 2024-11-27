class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        prefixsum = {0:1}
        res = 0
        currsum = 0

        for num in nums:
            currsum+=num
            if currsum - goal in prefixsum:
                res+=prefixsum[currsum-goal]
            if currsum in prefixsum:
                prefixsum[currsum]+=1
            else:
                prefixsum[currsum]=1
        return res
