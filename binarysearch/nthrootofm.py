
def nthrootofm(x,n):
    l = 1
    r = x
    if x < 2:
        return x
    while l <= r:
        mid = (l+r)//2
        
        val = mid ** n 
        if val == x:
            return mid
        if val < x:
            l = mid+1
        else:
            r = mid-1
    return -1

n = 3
m = 27
ans = nthrootofm(m, n)
print("The answer is:", ans)
