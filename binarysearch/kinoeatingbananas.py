
import math

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def canfinish(speed):
            totalhrs = 0
            for pile in piles:
                # Calculate hours needed for each pile at the current speed
                totalhrs += math.ceil(pile / speed)
            return totalhrs <= h

        low = 1
        high = max(piles)
        ans = high

        while low <= high:
            mid = (low + high) // 2
            if canfinish(mid):
                ans = mid  # Update the answer to the current speed
                high = mid - 1  # Try smaller speeds
            else:
                low = mid + 1  # Try larger speeds

        return ans

solution = Solution()
piles = [3, 6, 7, 11]
h = 8
result = solution.minEatingSpeed(piles, h)
print(result)  # Output: The minimum eating speed required.
