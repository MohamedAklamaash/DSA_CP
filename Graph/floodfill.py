
def floodfill(grid,sr,sc,newcolor):
    if not grid:
        return 0
    rows,cols = len(grid),len(grid[0])
    orgcolor = grid[sr][sc]
    def dfs(r,c):
        if r < 0 or r >= rows or c < 0 or c>= cols: 
            return
        if grid[r][c] != orgcolor:
            return
        grid[r][c] = newcolor
        dfs(r-1,c)
        dfs(r+1,c)
        dfs(r,c-1)
        dfs(r,c+1)
    dfs(sr,sc)
    return grid

# Example image (2D grid)
image = [
    [1, 1, 1],
    [1, 1, 0],
    [1, 0, 1]
]

# Starting point (1, 1) and new color (2)
sr, sc, new_color = 1, 1, 2

# Call Flood Fill
result_dfs = floodfill(image, sr, sc, new_color)
print("Flood Fill (DFS):")
print(result_dfs)


