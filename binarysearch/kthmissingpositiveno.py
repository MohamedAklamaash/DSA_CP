
class Solution(object):
    def findKthPositive(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        l = 0
        r = len(arr)-1

        while l <= r:
            mid = (l+r)//2
            if arr[mid]-(mid+1)<k:
                low = mid+1
            else:
                high = mid-1
        return l+k
