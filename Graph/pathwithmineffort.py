import heapq

def pathwithmineffort(adjmat):
    rows,cols = len(adjmat),len(adjmat[0])
    srcrow,srccol = 0,0
    destrow,destcol = rows-1,cols-1
    pq = [(0,srcrow,srccol)]
    if (
        srcrow < 0 or srcrow >= rows or srccol < 0 or srccol >= cols or
        destrow < 0 or destrow >= rows or destcol < 0 or destcol >= cols
    ):
        return -1, []
    distance = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    distance[srcrow][srccol] = 0
    parent = {(srcrow,srccol):None}
    while pq:
        curr_dist,curr_row,curr_col = heapq.heappop(pq)
        if curr_row == destrow and curr_col == destcol:
            node = (curr_row,curr_col)
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return curr_dist,path[::-1]
        for dr,dc in [(-1,0),(1,0),(0,1),(0,-1)]:
            nr,nc = curr_row+dr,curr_col+dc
            if 0 <= nr < rows and 0 <= nc < cols:
                dist = max(curr_dist,abs(adjmat[nr][nc] - adjmat[curr_row][curr_col])) 
                if dist < distance[nr][nc]:
                    distance[nr][nc] = dist
                    heapq.heappush(pq,(dist,nr,nc))
                    parent[(nr,nc)] = (curr_row,curr_col)
    return -1,[]

grid = [
    [1, 2, 2],
    [3, 8, 2],
    [5, 3, 5]
]

effort, path = pathwithmineffort(grid)
print(f"Minimum Effort: {effort}")
print(f"Path: {path}")
