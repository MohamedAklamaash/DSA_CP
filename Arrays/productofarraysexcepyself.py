
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        prefix = 1
        postfix = 1
        n = len(nums)

        for i in range(n):
            res.append(prefix)
            prefix*=nums[i]
        
        for i in range(n-1,-1,-1):
            res[i]*=postfix
            postfix*=nums[i]
        return res

