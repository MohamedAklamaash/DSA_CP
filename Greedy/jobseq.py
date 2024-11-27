
def jobseq(arr):
    if not arr:
        return -1
    # arr contains id at 0, deadline at 1 and profit at 2
    arr.sort(key = lambda  x: x[2],reverse=True)
    n = len(arr)
    schedule = [-1] * (n+1)
    
    for id,deadline,_ in arr:
        if schedule[deadline]==-1:
            schedule[deadline] = id
        elif schedule[deadline]!=-1:
            flag = False
            for i in range(deadline-1,0,-1):
                if schedule[i]==-1:
                    schedule[i] = id
                    flag = True
                    break
    return schedule
jobs = [
    [1, 4, 20],
    [2, 1, 10],
    [3, 1, 40],
    [4, 1, 30]
]

print(jobseq(jobs))

