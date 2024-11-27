
def nonoverlappingintervals(arr):
    if not arr:
        return None
    arr.sort(key = lambda x:x[1])
    prevstart = -1
    prevend = -1
    ans = []
    for u,v in arr:
        if prevstart == -1 and prevend == -1:
            prevstart = u
            prevend = v
            ans.append((u,v))
        elif prevend <= u:
            prevstart = u
            prevend = v
            ans.append((u,v))
    return len(arr) - len(ans)


