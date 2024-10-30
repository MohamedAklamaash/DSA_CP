from collections import deque

def rottenorange(grid):
    if not grid:
        return -1
    rows,cols = len(grid),len(grid[0])

    queue = deque()
    freshcount = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                freshcount+=1
            elif grid[i][j] == 2:
                queue.append((i,j))
    mins = 0
    while queue and freshcount > 0:
        r,c = queue.popleft()
        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            nr,nc = r+dr,c+dc
            if 0 <= nr < rows and 0 <=nc < cols and grid[nr][nc] == 1:
                grid[nr][nc] = 2
                freshcount-=1
                queue.append((nr,nc))
        mins+=1

    return mins

grid = [
    [2, 1, 1],
    [1, 1, 0],
    [0, 1, 2]
]

result = rottenorange(grid)
print("Minimum minutes until all oranges are rotten:", result)
