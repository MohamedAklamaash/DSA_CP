
def dfs(r,c,rows,cols,visited,graph):
    if r < 0 or r >= rows or c < 0 or c>= cols or graph[r][c] == 0 or visited[r][c] == 1:
        return
    visited[r][c] = 1
    dfs(r-1,c,rows,cols,visited,graph)
    dfs(r+1,c,rows,cols,visited,graph)
    dfs(r,c-1,rows,cols,visited,graph)
    dfs(r,c+1,rows,cols,visited,graph)
    
def noofenclaves(graph):
    if not graph:
        return 0
    rows,cols = len(graph),len(graph[0])
    visited = [[0 for _ in range(cols)] for _ in range(rows)]
    # first row and last row
    for i in range(cols):
        if graph[0][i] == 1 and visited[0][i] == 0:
            dfs(0,i,rows,cols,visited,graph)
        if graph[rows-1][i] == 1 and visited[rows-1][i] == 0:
            dfs(rows-1,i,rows,cols,visited,graph)

    for i in range(cols):
        if graph[i][0] == 1 and visited[i][0] == 0:
            dfs(i,0,rows,cols,visited,graph)
        if graph[i][cols-1] == 1 and visited[i][cols-1] == 0:
            dfs(i,cols-1,rows,cols,visited,graph)

    count = 0
    for i in range(rows):
        for j in range(cols):
            if graph[i][j] == 1 and visited[i][j] == 0:
                count+=1
    return count

if __name__ == "__main__":
    # Define test cases
    test_cases = [
        { 
            "input": [
                [0, 0, 0, 0],
                [1, 0, 1, 0],
                [0, 1, 1, 0],
                [0, 0, 0, 0]
            ],
            "expected": 3
        },
        {
            "input": [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            "expected": 0
        },
        {
            "input": [
                [1, 1, 1],
                [1, 1, 1],
                [1, 1, 1]
            ],
            "expected": 0
        },
        {
            "input": [],
            "expected": 0
        },
        {
            "input": [
                [0, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            "expected": 1
        }
    ]

    # Run tests
    for idx, test in enumerate(test_cases):
        print(f"Test Case {idx + 1}:")
        graph = test["input"]
        expected = test["expected"]
        
        print("Input Graph:")
        for row in graph:
            print(row)
        
        output = noofenclaves(graph)
        print("Output:", output)
        print("Expected:", expected)
        print("Result:", "Pass" if output == expected else "Fail")
        print("-" * 30)

