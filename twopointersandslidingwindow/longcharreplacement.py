class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0  
        freq = {}  
        max_count = 0  
        max_length = 0 

        for r in range(len(s)):
            freq[s[r]] = freq.get(s[r], 0) + 1
            max_count = max(max_count, freq[s[r]])
            if (r - l + 1) - max_count > k:
                freq[s[l]] -= 1
                l += 1
            max_length = max(max_length, r - l + 1)
        return max_length

