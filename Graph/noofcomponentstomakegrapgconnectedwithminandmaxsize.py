

def componentsInGraph(gb):
    def findParent(x, parent):
        if x != parent[x]:
            parent[x] = findParent(parent[x], parent)
        return parent[x]
    
    def unionbyrank(u, v, rank, parent):
        rootX = findParent(u, parent)
        rootY = findParent(v, parent)
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

    n = len(gb)
    rank = [0] * (2 * n + 1)
    parent = [i for i in range(2 * n + 1)]
    nodes = set()  # To track all nodes
    for u, v in gb:
        nodes.add(u)
        nodes.add(v)
    for u, v in gb:
        unionbyrank(u,v,rank,parent)
    component_sizes = {}
    for node in nodes:
        root = findParent(node, parent)
        if root not in component_sizes:
            component_sizes[root] = 0
        component_sizes[root] += 1
    
    # Get min and max component sizes
    sizes = list(component_sizes.values())
    return min(sizes), max(sizes)


