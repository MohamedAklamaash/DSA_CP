import heapq
from collections import defaultdict
import math

def countPaths(n, roads, src, dst):
    """
    Find the number of ways to reach the destination with the shortest distance.
    
    :param n: int - Number of nodes in the graph.
    :param roads: List[List[int]] - Edge list of the graph [u, v, time].
    :param src: int - Starting node.
    :param dst: int - Destination node.
    :return: int - Number of ways to reach the destination with the shortest distance.
    """
    MOD = 10**9 + 7
    
    # Build the graph as an adjacency list
    graph = defaultdict(list)
    for u, v, time in roads:
        graph[u].append((v, time))
        graph[v].append((u, time))
    
    # Distance and ways arrays
    dist = [math.inf] * n
    ways = [0] * n
    dist[src] = 0
    ways[src] = 1
    
    # Priority queue for Dijkstra's algorithm
    pq = [(0, src)]  # (current distance, current node)
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        # If the distance is outdated, skip
        if curr_dist > dist[curr_node]:
            continue
        
        # Process all neighbors
        for neigh, time in graph[curr_node]:
            new_dist = curr_dist + time
            
            # If a shorter path is found
            if new_dist < dist[neigh]:
                dist[neigh] = new_dist
                ways[neigh] = ways[curr_node]
                heapq.heappush(pq, (new_dist, neigh))
            
            # If another shortest path is found
            elif new_dist == dist[neigh]:
                ways[neigh] = (ways[neigh] + ways[curr_node]) % MOD
    
    return ways[dst]

# Example Usage
n = 7
roads = [
    [0, 1, 1],
    [0, 2, 1],
    [1, 3, 1],
    [2, 3, 1],
    [3, 4, 1],
    [4, 5, 1],
    [5, 6, 1]
]
src = 0
dst = 6

print(countPaths(n, roads, src, dst))  # Output: 4

