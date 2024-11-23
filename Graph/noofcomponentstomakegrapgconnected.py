def findParent(x, parent):
    if x != parent[x]:
        parent[x] = findParent(parent[x], parent)  # Path compression
    return parent[x]

def union(x, y, parent, rank):
    rootX = findParent(x, parent)
    rootY = findParent(y, parent)
    if rootX != rootY:
        if rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        elif rank[rootY] < rank[rootX]:
            parent[rootY] = rootX
        else:
            parent[rootY] = rootX
            rank[rootX] += 1
        return True
    return False

def makeConnected(n, connections):
    # If there aren't enough edges, return -1
    if len(connections) < n - 1:
        return -1

    # Initialize DSU
    parent = [i for i in range(n)]
    rank = [0 for _ in range(n)]
    components = n  # Initially, every node is its own component

    # Perform unions
    for u, v in connections:
        if union(u, v, parent, rank):  # If nodes are successfully connected
            components -= 1

    # The number of operations needed is (components - 1)
    return components - 1

