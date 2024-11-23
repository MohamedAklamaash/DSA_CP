from collections import defaultdict
import heapq

def shortestpathinweightedundirgraph(graph, n, src=1, target=None):
    """
    Finds the shortest distance and path in a weighted undirected graph from src to target.

    :param graph: defaultdict(list), adjacency list where each key maps to a list of (neighbor, weight)
    :param n: int, total number of nodes
    :param src: int, source node (default is 1)
    :param target: int, target node (default is None, meaning compute for all nodes)
    :return: tuple (distance, path) to the target node, or (-1, []) if unreachable
    """
    if n == 0 or not graph:
        return -1, []

    if src == target:
        return 0, [src]

    distance = {node: float("inf") for node in range(1, n + 1)}
    distance[src] = 0
    pred = {node: -1 for node in range(1, n + 1)}
    pq = [(0, src)]  # Priority queue with (distance, node)

    while pq:
        curr_dist, curr_node = heapq.heappop(pq)

        # Stop early if we've reached the target
        if curr_node == target:
            path = []
            while curr_node != -1:
                path.append(curr_node)
                curr_node = pred[curr_node]
            return curr_dist, path[::-1]  # Return distance and reversed path

        if curr_dist > distance[curr_node]:
            continue

        for neigh, weight in graph[curr_node]:
            dist = curr_dist + weight
            if dist < distance[neigh]:
                distance[neigh] = dist
                pred[neigh] = curr_node
                heapq.heappush(pq, (dist, neigh))

    # If the target is specified but unreachable
    if target:
        return -1, []

    # Return distances for all nodes if no target is specified
    return {node: (distance[node] if distance[node] != float("inf") else -1) for node in range(1, n + 1)}


