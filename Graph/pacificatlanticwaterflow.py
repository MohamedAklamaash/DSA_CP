class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """

        pacificset = set()
        atlanticset = set()
        rows,cols = len(heights),len(heights[0])
        def dfs(r,c,visited,prevheight):
            if r < 0 or r >= rows or c < 0 or c>=cols or (r,c) in visited or heights[r][c] < prevheight:
                return
            visited.add((r,c))
            dfs(r-1,c,visited,heights[r][c])
            dfs(r+1,c,visited,heights[r][c])
            dfs(r,c-1,visited,heights[r][c])
            dfs(r,c+1,visited,heights[r][c])

        for i in range(rows):
            dfs(i, 0, pacificset, heights[i][0]) 
        for j in range(cols):
            dfs(0, j, pacificset, heights[0][j]) 

        for i in range(rows):
            dfs(i, cols - 1, atlanticset, heights[i][cols - 1]) 
        for j in range(cols):
            dfs(rows - 1, j, atlanticset, heights[rows - 1][j])
        res = []
        for i in range(rows):
            for j in range(cols):
                if (i,j) in pacificset and (i,j) in atlanticset:
                    res.append([i,j])
        return res
