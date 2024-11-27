
def longsubstrwithkchrs(s,k):
    if not s:
        return 0
    l = 0
    freq = {}
    maxi = 0
    for r in range(len(s)):
        if s[r] not in freq:
            freq[s[r]]=1
        else:
            freq[s[r]]+=1

        if len(freq) > k:
            while len(freq) > k:
                freq[s[l]]-=1
                if freq[s[l]] == 0:
                    del freq[s[l]]
                l+=1
        maxi = max(maxi,r-l+1)
    return maxi

