def isbipartite_dfs(graph):
    def dfs(node, c):
        color[node] = c  # Assign color `c` to the current node
        for neigh in graph[node]:
            if color[neigh] == -1:  # If neighbor is uncolored
                if not dfs(neigh, 1 - c):  # Recur with the opposite color
                    return False
            elif color[neigh] == c:  # If neighbor has the same color
                return False
        return True
    
    if not graph:
        return True  # An empty graph is trivially bipartite
    
    color = [-1] * len(graph)  # Initialize all nodes as uncolored (-1)
    
    for start in range(len(graph)):  # Handle disconnected components
        if color[start] == -1:  # If the node is unvisited
            if not dfs(start, 0):  # Start DFS with color 0
                return False
    
    return True

