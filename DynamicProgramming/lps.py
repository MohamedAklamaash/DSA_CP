
class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]
        def f(i,j,s1,s2):
            if i >= n or j >= n:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            matchcase,skip1,skip2 = 0,0,0
            if s1[i] == s2[j]:
                matchcase = 1 + f(i+1,j+1,s1,s2)
            else:
                skip1 = f(i+1,j,s1,s2)
                skip2 = f(i,j+1,s1,s2)
            
            dp[i][j] = max(matchcase,max(skip1,skip2))
            return dp[i][j]
        return f(0,0,s,s[::-1])
