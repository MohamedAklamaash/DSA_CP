from collections import deque,defaultdict
import heapq
def djisktra(graph,src):
    distances = {node:float("inf") for node in range(len(graph))}
    distances[src] = 0
    pq = [(0,src)]
    while pq:
        curr_dist,curr_node = heapq.heappop(pq)
        if distances[curr_node] < curr_dist:
            continue
        for neigh,weight in graph[curr_node]:
            dist = weight+ curr_dist
            if dist < distances[neigh]:
                distances[neigh] = dist
                heapq.heappush(pq,(dist,neigh))
    return distances
graph = {
    0: [(1, 4), (2, 1)],
    1: [(3, 1)],
    2: [(1, 2), (3, 5)],
    3: []
}

start_node = 0
shortest_distances = djisktra(graph, start_node)
print("Shortest distances from node 0:", shortest_distances)

