from collections import deque

def updatematrix(mat):
    if not mat:
        return mat
    queue = deque()
    rows,cols = len(mat),len(mat[0])
    res = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                queue.append((i,j))
                res[i][j] = 0

    while queue:
        r,c = queue.popleft()
        for dr,dc in [(-1,0),(1,0),(0,-1),(0,1)]:
            nr , nc = r +  dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and res[nr][nc] == float("inf"):
                res[nr][nc] = res[r][c]+1
                queue.append((nr,nc))
    return res

matrix = [
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
]

result = updatematrix(matrix)
print(result) 


