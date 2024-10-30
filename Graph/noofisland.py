def noofislands(grid):
    if not grid:
        return 0
    rows,cols = len(grid),len(grid[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    def dfs(r,c):
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0' or visited[r][c]:
            return 
        visited[r][c] = True
        dfs(r-1,c)
        dfs(r+1,c)
        dfs(r,c-1)
        dfs(r,c+1)
    count = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '1' and not visited[i][j]:
                dfs(i,j)
                count+=1
    return count

grid = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]

print("Number of Islands:", noofislands(grid))


