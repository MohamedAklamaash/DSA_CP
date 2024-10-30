from collections import deque

def detect_cycle(graph):
    if not graph:
        return graph
    visited = set()
    for start in graph:
        if start not in visited:
            queue= deque([(start,-1)])
            visited.add(start)
            while queue:
                node,parent = queue.popleft()
                for neigh in graph[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        queue.append((neigh,node))
                    elif neigh!=parent:
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
print(detect_cycle(graph))  # Output: True

