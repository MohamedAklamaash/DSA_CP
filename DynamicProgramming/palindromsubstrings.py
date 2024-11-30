
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        memo = {}

        def f(i,j):
            if i >= j:
                return True
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = False
            if s[i] == s[j]:
                memo[(i,j)] = f(i+1,j-1)
            return memo[(i,j)]
        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i,n):
                if f(i,j):
                    res+=1
        return res

