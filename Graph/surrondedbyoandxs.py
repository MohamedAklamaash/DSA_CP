def dfs(r, c, rows, cols, graph, visited):
    # Base case: Out of bounds, already visited, or not an "O"
    if r < 0 or r >= rows or c < 0 or c >= cols or graph[r][c] != "O" or visited[r][c] == 1:
        return
    visited[r][c] = 1
    # Explore in all four directions
    dfs(r - 1, c, rows, cols, graph, visited)
    dfs(r + 1, c, rows, cols, graph, visited)
    dfs(r, c - 1, rows, cols, graph, visited)
    dfs(r, c + 1, rows, cols, graph, visited)

def surroundedbyxandos(graph):
    if not graph or not graph[0]:
        return -1  # Handle invalid or empty input
    
    rows, cols = len(graph), len(graph[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]

    # Step 1: Traverse boundary cells and mark connected "O"s
    for i in range(cols):  # First and last row
        if graph[0][i] == "O" and visited[0][i] == 0:
            dfs(0, i, rows, cols, graph, visited)
        if graph[rows - 1][i] == "O" and visited[rows - 1][i] == 0:
            dfs(rows - 1, i, rows, cols, graph, visited)

    for i in range(rows):  # First and last column
        if graph[i][0] == "O" and visited[i][0] == 0:
            dfs(i, 0, rows, cols, graph, visited)
        if graph[i][cols - 1] == "O" and visited[i][cols - 1] == 0:
            dfs(i, cols - 1, rows, cols, graph, visited)

    # Step 2: Mark all unvisited "O"s as "X"
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == "O" and visited[i][j] == 0:
                graph[i][j] = "X"
    
    return graph

# Main function to test
if __name__ == "__main__":
    graph = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]

    print("Original Graph:")
    for row in graph:
        print(row)

    result = surroundedbyxandos(graph)

    print("\nProcessed Graph:")
    print(result)  
 

