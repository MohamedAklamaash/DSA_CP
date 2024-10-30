from collections import deque

def hascycledfs(graph):
    if not graph:
        return graph
    visited = set()
    def dfs(node,parent):
        visited.add(node)
        for neigh in graph[node]:
            if neigh not in visited:
                if dfs(neigh,node):
                    return True
                if neigh!=parent:
                    return True
        return False
    
    for start in graph:
        if start not in visited:
            if dfs(start,-1):
                return True
    return False

# Define an undirected graph as an adjacency list
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

# Check if the graph contains a cycle
print(hascycledfs(graph))  # Output: True


