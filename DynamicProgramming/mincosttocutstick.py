
class Solution(object):
    def minCost(self, n, cuts):
        """
        :type n: int
        :type cuts: List[int]
        :rtype: int
        """
        cuts.sort()
        cuts = [0] + cuts + [n]
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        def mcm(i,j):
            if i+1 == j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini = float("inf")
            for k in range(i+1,j):
                cost = cuts[j] - cuts[i] + mcm(i, k) + mcm(k, j)
                mini = min(mini,cost)
            dp[i][j] = mini
            return mini
        return mcm(0,len(cuts)-1)

