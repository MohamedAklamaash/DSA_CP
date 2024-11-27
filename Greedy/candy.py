class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """

        def func(arr):
            if not arr:
                return []
            
            candies = [1]
            for i in range(1,len(arr)):
                if arr[i-1] < arr[i]:
                    candies.append(candies[-1]+1)
                else:
                    candies.append(1)
            return candies
        left = func(ratings)
        right = func(ratings[::-1])
        right = right[::-1]
        res = 0
        for i in range(len(left)):
            res+= max(left[i],right[i])
        return res
