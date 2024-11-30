class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m,n = len(word1),len(word2)
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        def mineditdistance(i,j,s1,s2):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            insert,delete,update = 0,0,0
            if dp[i][j]!=-1:
                return dp[i][j]
            if s1[i] == s2[j]:
                return mineditdistance(i-1,j-1,s1,s2)
            else:
                insert = mineditdistance(i,j-1,s1,s2)
                delete = mineditdistance(i-1,j,s1,s2)
                update = mineditdistance(i-1,j-1,s1,s2)
            dp[i][j] = 1 + min(delete,update,insert)
            return dp[i][j]
        return mineditdistance(len(word1)-1,len(word2)-1,word1,word2)
