from collections import deque

def isbipartite(graph):
    if not graph:
        return True
    color = [-1] * len(graph)
    queue = deque()
    for start in range(len(graph)):
        if color[start] == -1:
            color[start] = 0
            queue.append(start)
            while queue:
                node = queue.popleft()
                for neigh in graph[node]:
                    if color[neigh] == -1:
                        color[neigh] = 1 - color[node]
                        queue.append(neigh)
                    elif color[neigh] == color[node]:
                        return False
    return True

if __name__ == "__main__":
    # Example test cases
    test_graphs = [
        ([[], [2, 4], [1, 3], [2, 4], [1, 3]], True),  # Bipartite
        ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),  # Not bipartite
        ([[], []], True),  # Bipartite (two isolated nodes)
        ([], True)  # Bipartite (empty graph)
    ]

    for idx, (graph, expected) in enumerate(test_graphs):
        result = isbipartite(graph)
        print(f"Test Case {idx + 1}: {'Pass' if result == expected else 'Fail'}")

