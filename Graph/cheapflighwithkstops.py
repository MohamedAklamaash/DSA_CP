import heapq

def shortestflightwithkstops(graph,src,dst,k):
    if not graph:
        return -1,[]
    rows = len(graph)
    distance = [float("inf") for _ in range(rows)]
    distance[src] = 0
    parent = {src:None}
    pq = [(0,src,0)] # dist,curr node , no of stops taken
    while pq:
        curr_dist,curr_node,stops = heapq.heappop(pq)
        if curr_node == dst and stops <= k:
            path = []
            while curr_node:
                path.append(curr_node)
                curr_node = parent[curr_node]
            return curr_dist,path[::-1]
        if stops > k:
            continue
        for neigh,cost in graph[curr_node]:
            dist = cost + curr_dist
            if distance[neigh] > dist and stops<k:
                distance[neigh] = dist
                heapq.heappush(pq,(dist,neigh,stops+1))
                parent[neigh] = curr_node
    return -1,[]

# Example usage
graph = {
    0: [(1, 100), (2, 500)],  # 0 -> 1 (100), 0 -> 2 (500)
    1: [(2, 100)],            # 1 -> 2 (100)
    2: []                     # 2 has no outgoing flights
}

src = 0
dst = 2
k = 1

distance, path = shortestflightwithkstops(graph, src, dst, k+1)
print(f"Distance: {distance}, Path: {path}")
