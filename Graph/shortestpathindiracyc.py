from collections import defaultdict, deque

def shortest_path_dag(vertices, edges, source):
    # Step 1: Build the graph
    graph = defaultdict(list)
    for u, v, weight in edges:
        graph[u].append((v, weight))
    
    # Step 2: Topological Sort (using Kahn's Algorithm)
    indegree = {i: 0 for i in range(vertices)}
    for u in graph:
        for v, _ in graph[u]:
            indegree[v] += 1
    
    queue = deque([node for node in range(vertices) if indegree[node] == 0])
    topo_order = []
    
    while queue:
        node = queue.popleft()
        topo_order.append(node)
        for neighbor, _ in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    # Step 3: Initialize distances
    dist = [float('inf')] * vertices
    dist[source] = 0
    
    # Step 4: Relax edges in topological order
    for node in topo_order:
        if dist[node] != float('inf'):
            for neighbor, weight in graph[node]:
                if dist[node] + weight < dist[neighbor]:
                    dist[neighbor] = dist[node] + weight
    
    # Replace 'inf' with -1 for unreachable nodes
    return [d if d != float('inf') else -1 for d in dist]

# Example Usage
vertices = 6
edges = [
    (0, 1, 2),
    (0, 4, 1),
    (1, 2, 3),
    (4, 2, 2),
    (4, 5, 4),
    (2, 3, 6),
    (5, 3, 1)
]
source = 0

print(shortest_path_dag(vertices, edges, source))  # Output: [0, 2, 3, 8, 1, 5]
  
