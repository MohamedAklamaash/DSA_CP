class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x:x[0])

        merged = [intervals[0]]

        for curr in intervals[1:]:
            prev = merged[-1]
            if curr[0] <= prev[1]:
                merged[-1] = [prev[0],max(prev[1],curr[1])]
            else:
                merged.append(curr)
        print(merged)
        return merged
