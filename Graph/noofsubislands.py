class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        
        rows, cols = len(grid1), len(grid1[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] == 0 or visited[r][c] == 1:
                return True
            visited[r][c] = 1
            issubisland = grid1[r][c] == 1
            issubisland&=dfs(r-1,c)
            issubisland&=dfs(r+1,c)
            issubisland&=dfs(r,c-1)
            issubisland&=dfs(r,c+1)
            return issubisland
        
        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid2[i][j] == 1 and visited[i][j] == 0:
                    if dfs(i,j):
                        res+=1
        return res