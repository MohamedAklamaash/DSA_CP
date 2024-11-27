class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        def atmostk(k):
            l = 0
            freq = {}
            res = 0
            for r in range(len(nums)):
                if nums[r] not in freq:
                    freq[nums[r]] = 1
                else:
                    freq[nums[r]] +=1
                while len(freq) > k:
                    freq[nums[l]]-=1
                    if freq[nums[l]] == 0:
                        del freq[nums[l]]
                    l+=1
                res += r-l+1
            return res
        return atmostk(k) - atmostk(k-1) # removes overlapping
