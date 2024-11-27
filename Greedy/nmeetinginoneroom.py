
def nmeeingsinoneroom(start, end):
    if not start or not end:
        return None
    res = []
    for u,v in zip(start,end):
        res.append((u,v))

    res.sort(key= lambda x:x[1]) # sorting based on the end timings
    prevstart = -1
    prevend = -1
    ans = []
    for u,v in res:
        if prevstart == -1 and prevend == -1:
            prevstart = u
            prevend =  v
            ans.append((u,v))
        elif prevend <= u:
            prevstart = u
            prevend = v
            ans.append((u,v))
    return ans

start = [0,3,1,5,5,8]
end = [5,4,2,9,7,9]
# len of start should be eql to the len of end

print(nmeeingsinoneroom(start,end))
