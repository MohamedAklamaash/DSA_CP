
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i = len(nums) -2

        while i >=0 and nums[i] >= nums[i+1]:
            i-=1
        if i!=-1:
            j = len(nums)-1
            while j>=0 and nums[j] <= nums[i]:
                j-=1
            nums[j],nums[i] = nums[i],nums[j]
        nums[i+1:] = reversed(nums[i+1:])