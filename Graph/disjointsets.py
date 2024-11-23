def findParent(x, parent):
    if x != parent[x]:
        parent[x] = findParent(parent[x], parent)  # Path compression
    return parent[x]

def unionbyrank(x, y, rank, parent):
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

def unionbysize(x, y, size, parent):
    rootX = findParent(x, parent)
    rootY = findParent(y, parent)
    if rootX != rootY:
        if size[rootX] < size[rootY]:
            size[rootY] += size[rootX]  # Add size of rootX to rootY
            parent[rootX] = rootY
        else:
            size[rootX] += size[rootY]  # Add size of rootY to rootX
            parent[rootY] = rootX

# Initialize
n = 10
rank = [0 for _ in range(n)]  # Rank for Union by Rank
size = [1 for _ in range(n)]  # Size for Union by Size
parent = [i for i in range(n)]  # Parent array for all elements

# Example Operations
unionbyrank(1, 2, rank, parent)
unionbyrank(3, 4, rank, parent)
unionbysize(2, 3, size, parent)

# Find Operations
print(findParent(2, parent))  # Output: root of set containing 2
print(findParent(4, parent))  # Output: root of set containing 4
print(parent)  # Show the parent array after unions
print(size)  # Show the size array after unions

