class Solution(object):
    def countSubIslands(self, grid1, grid2):
        """
        :type grid1: List[List[int]]
        :type grid2: List[List[int]]
        :rtype: int
        """
        rows, cols = len(grid1), len(grid1[0])
        
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols or grid2[r][c] == 0:
                return True
            
            grid2[r][c] = 0  # Mark as visited
            is_sub_island = grid1[r][c] == 1  # Check if cell is valid in grid1
            
            # Explore all four directions
            for dr, dc in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                is_sub_island &= dfs(r + dr, c + dc)
            
            return is_sub_island
        
        count = 0
        for i in range(rows):
            for j in range(cols):
                # Start DFS if it's part of an island in grid2
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        
        return count

