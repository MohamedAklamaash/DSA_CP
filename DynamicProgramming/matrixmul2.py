
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        def matmul(arr,i,j):
            if i+1 == j:
                return 0
            
            minmul = float("-inf")
            for k in range(i+1,j):
                count = matmul(arr,i,k) + matmul(arr,k,j) + arr[i]*arr[k]*arr[j]
                minmul = max(minmul, count)
            return minmul
        return matmul(nums,0,len(nums)-1)

