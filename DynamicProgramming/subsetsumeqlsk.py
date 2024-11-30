
def subsetsumeqlsk(ind,target,arr):
    if target == 0:
        return True
    if ind == 0:
        return arr[0] == target
    
    nottake = subsetsumeqlsk(ind-1,target,arr)
    take = False
    if arr[ind] <= target:
        take = subsetsumeqlsk(ind-1,target-arr[ind],arr)
    return take or nottake

arr = [3, 34, 4, 12, 5, 2]
target = 9
n = len(arr)

result = subsetsumeqlsk(n - 1, target, arr)
print(f"Is there a subset with sum {target}? {'Yes' if result else 'No'}")

