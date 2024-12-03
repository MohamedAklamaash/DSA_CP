
from heapq import heappop, heappush
from collections import defaultdict

def synchronousShopping(n, k, centers, roads):
    # Convert fish types at each center into sets
    fish_at_shop = [set(centers[i]) for i in range(n)]

    # Build the graph
    graph = defaultdict(list)
    for u, v, t in roads:
        graph[u - 1].append((v - 1, t))
        graph[v - 1].append((u - 1, t))

    # Priority queue for Dijkstra's: (time, node, fish_set)
    pq = [(0, 0, fish_at_shop[0])]  # Start at node 0
    # Distance table: min_time[node][fish_set]
    min_time = defaultdict(lambda: defaultdict(lambda: float('inf')))
    min_time[0][frozenset(fish_at_shop[0])] = 0

    # Dijkstra's algorithm
    while pq:
        time, node, fish_set = heappop(pq)

        # If we already have a shorter time for this state, skip
        if time > min_time[node][frozenset(fish_set)]:
            continue

        # Traverse neighbors
        for neighbor, weight in graph[node]:
            new_time = time + weight
            new_fish_set = fish_set | fish_at_shop[neighbor]  # Union of fish sets

            if new_time < min_time[neighbor][frozenset(new_fish_set)]:
                min_time[neighbor][frozenset(new_fish_set)] = new_time
                heappush(pq, (new_time, neighbor, new_fish_set))

    # Merge states at the destination node
    all_fish = set(range(1, k + 1))  # All fish types
    result = float('inf')
    destination_states = list(min_time[n - 1].items())

    for (fish_set1, time1) in destination_states:
        for (fish_set2, time2) in destination_states:
            if fish_set1 | fish_set2 == all_fish:
                result = min(result, max(time1, time2))

    return result

