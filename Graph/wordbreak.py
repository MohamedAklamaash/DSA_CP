def word_break_dp(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True  # Base case: Empty string can be broken

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]

# Example
s = "leetcode"
word_dict = {"leet", "code"}
print(word_break_dp(s, word_dict))  # Output: True
