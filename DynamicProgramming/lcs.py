
def lcs(i,j,s1,s2):
    if i >= len(s1) or j >= len(s2):
        return 0
    matchcase,skip1,skip2 = 0,0,0
    if(s1[i] == s2[j]):
        matchcase = 1 + lcs(i+1,j+1,s1,s2)
    else:
        skip1 = lcs(i+1,j,s1,s2)
        skip2 = lcs(i,j+1,s1,s2)
    return max(max(skip1,skip2),matchcase)

