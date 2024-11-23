from collections import deque
from typing import  List

def noofunqislands(grid:List[List[int]]):
    if not grid:
        return grid
    rows,cols = len(grid),len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(r:int,c:int,org_r:int,org_c:int,path):
        if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or grid[r][c] == 0:
            return
        visited[r][c] = True
        path.append((r-org_r,c - org_c))
        dfs(r-1,c,org_r,org_c,path)
        dfs(r+1,c,org_r,org_c,path)
        dfs(r,c-1,org_r,org_c,path)
        dfs(r,c+1,org_r,org_c,path)
    unique_islands = set()
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1 and not visited[i][j]:
                path = []
                dfs(i,j,i,j,path)
                unique_islands.add(tuple(path))
    return len(unique_islands)

grid = [
    [1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 1],
    [1, 1, 0, 1, 1]
]

print(noofunqislands(grid))  # Output: Number of distinct island shapes

