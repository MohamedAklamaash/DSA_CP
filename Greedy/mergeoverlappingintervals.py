
def mergeoverlappingintervals(intervals):
    intervals.sort(key = lambda x:x[0])
    
    merged = [intervals[0]]

    for curr in intervals[1:]:
        prev = merged[-1]
        if curr[0] <= prev[1]:
            merged[-1] = [prev[0],max(prev[1],curr[1])]
        else:
            merged.append(curr)
    return merged

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(mergeoverlappingintervals(intervals))
