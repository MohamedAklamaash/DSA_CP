
class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7 

        dp = [[-1 for _ in range(target + 1)] for _ in range(n + 1)]

        def f(dice, amt):
            if dice == 0:
                return 1 if amt == 0 else 0
            if amt < 0:
                return 0

            if dp[dice][amt] != -1:
                return dp[dice][amt]

            ways = 0
            for face in range(1, k + 1):  
                ways += f(dice - 1, amt - face)
                ways %= MOD  

            dp[dice][amt] = ways 
            return dp[dice][amt]

        return f(n, target)

