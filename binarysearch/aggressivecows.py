
def aggressiveCows(positions,k):

    def canplace(mindist):
        lastposition = positions[0]
        count=1
        for i in range(1,len(positions)):
            if positions[i]-lastposition >= mindist:
                count+=1
                lastposition = positions[i]
            if count >= k:
                return True
        return False

    positions.sort()
    l =1
    r = max(positions) - min(positions)
    #ans = -1
    while l<=r:
        mid = (l+r)//2
        if canplace(mid):
            l = mid+1
            #ans = mid
        else:
            r = mid-1
    return r
