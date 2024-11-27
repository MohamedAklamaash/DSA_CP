

class Solution(object):
    def numberOfSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        freq = {"a":-1, "b":-1, "c":-1}
        res = 0
        for i in range(n):
            freq[s[i]] = i

            minval = min(freq.values())
            if minval!=-1:
                res += minval+1
        
        return res
