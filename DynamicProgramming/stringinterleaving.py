class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        l,m,n = len(s1),len(s2),len(s3)
        dp = [[[-1 for _ in range(n+1)] for _ in range(m+1)] for _ in range(l+1) ]
        def f(i,j,k,s1,s2,s3):

            if i == len(s1) and j == len(s2) and k == len(s3):
                return True
            if dp[i][j][k] !=-1:
                return dp[i][j][k]
            if i == len(s1):
                return s2[j:] == s3[k:]
            if j == len(s2):
                return s1[i:] == s3[k:]
            
            takefroms1,takefroms2 = False, False
            if i < len(s1) and k < len(s3) and  s1[i] == s3[k]:
                takefroms1 = f(i+1,j,k+1,s1,s2,s3)
            if j < len(s2) and k < len(s3) and s2[j] == s3[k]:
                takefroms2 = f(i,j+1,k+1,s1,s2,s3)
            dp[i][j][k] = takefroms1 or takefroms2
            return dp[i][j][k]
        return f(0,0,0,s1,s2,s3)
