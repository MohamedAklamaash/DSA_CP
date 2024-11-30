
from collections import Counter
def maxwindowsubstr(s,t):
    if s == "" or t == "":
        return ""
    countT = Counter(t)
    have = 0
    need = len(countT)
    l = 0
    window = {}
    res = [-1, -1]
    reslen = float("inf")
    for r in range(len(s)):
        c = s[r]
        if c not in window:
            window[c] = 1
        else:
            window[c]+=1

        if c in countT and window[c] ==  countT[c]:
            have+=1

        while have == need:
            if r-l+1 < reslen:
                res =  [ l,r]
                reslen = r-l+1
            window[s[l]]-=1
            if s[l] in countT and window[s[l]] < countT[s[l]]:
                have-=1
            l+=1

    l,r = res
    return s[l:r+1] if reslen!=float("inf") else ""
