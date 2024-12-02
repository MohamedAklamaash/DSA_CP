
class Solution(object):
    def minDays(self, bloomDay, m, k):
        """
        :type bloomDay: List[int]
        :type m: int
        :type k: int
        :rtype: int
        """

        def canmakebouqonk(day):
            flowers = 0
            bouqets=0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers+=1
                    if flowers == k:
                        bouqets+=1
                        flowers = 0
                else:
                    flowers = 0
            return bouqets>=m

        l = 1
        r = max(bloomDay)
        ans = -1
        while l<=r:
            mid = (l+r)//2
            if canmakebouqonk(mid):
                ans = mid
                r = mid-1
            else:
                l = mid+1
        return ans

