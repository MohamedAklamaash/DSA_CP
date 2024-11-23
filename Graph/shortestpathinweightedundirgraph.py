from collections import defaultdict, deque
import heapq

def shortestpathinweightedundirgraph(graph,n,m):
    if not graph:
        return [-1]*m,[]
    src = 1
    distance = {node:float("inf") for node in range(1,n+1)}
    distance[src] = 0
    pq = [(0,src)]
    pred = {node:-1 for node in range(1,n+1)}
    while pq:
        curr_dist,curr_node = heapq.heappop(pq)
        
        if curr_node == n:
            path = []
            while curr_node!=-1:
                path.append(curr_node)
                curr_node = pred[curr_node]
            return curr_dist,path[::-1]

        if curr_dist > distance[curr_node]:
            continue
        
        for neigh,weight in graph[curr_node]:
            dist = weight + curr_dist
            if dist < distance[neigh]:
                distance[neigh] = dist
                pred[neigh] = curr_node
                heapq.heappush(pq,(dist,neigh))
    return [distance[node] if distance[node] != float("inf") else -1 for node in range(1, n + 1)] 
# Define an example graph as a defaultdict
graph = defaultdict(list)

# Add edges to the graph (undirected)
graph[1].append((2, 4))
graph[1].append((3, 1))
graph[2].append((1, 4))
graph[2].append((3, 2))
graph[3].append((1, 1))
graph[3].append((2, 2))

n = 1  # Total nodes
m = 3  # Total edges

# Find shortest paths
distances = shortestpathinweightedundirgraph(graph, n, m)
print(distances)  # Expected output: [0, 3, 1]``
