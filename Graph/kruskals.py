# Helper functions for Disjoint Set
def findParent(x, parent):
    if x != parent[x]:
        parent[x] = findParent(parent[x], parent)  # Path compression
    return parent[x]

def union(x, y, rank, parent):
    rootX = findParent(x, parent)
    rootY = findParent(y, parent)

    if rootX != rootY:  # Only union if they are in different sets
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootY] < rank[rootX]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

# Kruskal's algorithm
def kruskal(n, edges):
    # Initialize Disjoint Set
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]

    # Sort edges by weight
    edges.sort(key=lambda x: x[2])  # x[2] is the weight of the edge

    mst = []  # To store edges in the MST
    mst_cost = 0

    for u, v, w in edges:
        if findParent(u, parent) != findParent(v, parent):  # If adding edge doesn't form a cycle
            union(u, v, rank, parent)  # Merge sets
            mst.append((u, v, w))  # Add edge to MST
            mst_cost += w

    return mst, mst_cost

# Example usage
n = 7  # Number of vertices (0 to 6)
edges = [
    (0, 1, 7),  # (u, v, weight)
    (0, 3, 5),
    (1, 3, 9),
    (1, 2, 8),
    (1, 4, 7),
    (3, 4, 15),
    (2, 4, 5),
    (4, 5, 6),
    (5, 6, 8),
    (4, 6, 9)
]

mst, cost = kruskal(n, edges)
print("Edges in MST:", mst)
print("Total cost of MST:", cost)

