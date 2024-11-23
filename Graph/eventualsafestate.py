def eventualsafestate(graph):
    if not graph:
        return 0
    def dfs(graph,node,visited,pathvisited,check):
        visited[node] = 1
        pathvisited[node] = 1
        for neigh in graph[node]:
            if visited[neigh] == 0:
                if dfs(graph,neigh,visited,pathvisited,check):
                    check[node] = 0
                    return True
            elif pathvisited[neigh]:
                check[node] = 0
                return True
        pathvisited[node] = 0
        check[node] = 1
        return False
    
    visited = [0] * len(graph)
    pathvisited = [0] * len(graph)
    check = [0] * len(graph)
    for i in range(len(graph)):
        if visited[i] == 0:
            dfs(graph,i,visited,pathvisited,check)
    safenodes = []
    for i in range(len(check)):
        if check[i] == 1:
            safenodes.append(i)
    print(safenodes)
    return safenodes
if __name__ == "__main__":
    test_graphs = [
        ([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]),  # Safe nodes: [2, 4, 5, 6]
        ([[1, 2], [2, 3], [3], [4], [0]], []),  # Cycle present, no safe nodes
        ([[], [0], [1, 2], [1]], [0, 1, 2, 3]),  # All nodes are safe
        ([[], [2], [3], [4], []], [0, 1, 2, 3, 4]),  # All nodes are safe
        ([[], [], [], []], [0, 1, 2, 3]),  # Empty graph
    ]

    for idx, (graph, expected) in enumerate(test_graphs):
        result = eventualsafestate(graph)
        print(f"Test Case {idx + 1}: {'Pass' if result == expected else 'Fail'}")

