
from collections import defaultdict, deque

def journeyToMoon(n, astronaut_pairs):
    # Step 1: Build the graph
    graph = defaultdict(list)
    for u, v in astronaut_pairs:
        graph[u].append(v)
        graph[v].append(u)

    # Step 2: Find connected components using BFS
    visited = [False] * n
    def bfs(node):
        queue = deque([node])
        visited[node] = True
        size = 0
        while queue:
            current = queue.popleft()
            size += 1
            for neighbor in graph[current]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)
        return size

    # Get the size of each connected component
    sizes = []
    for i in range(n):
        if not visited[i]:
            sizes.append(bfs(i))

    # Step 3: Calculate valid pairs
    total_pairs = n * (n - 1) // 2  # Total possible pairs
    invalid_pairs = sum(size * (size - 1) // 2 for size in sizes)  # Pairs within the same country
    valid_pairs = total_pairs - invalid_pairs

    return valid_pairs

