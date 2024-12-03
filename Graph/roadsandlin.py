

from collections import defaultdict

def roadsAndLibraries(n, c_lib, c_road, cities):
    # Write your code here
        
    def findParent(x,parent):
        if x!=parent[x]:
            parent[x] = findParent(parent[x],parent)
        return parent[x]
    
    def unionbyrank(u,v,rank,parent):
        rootX = findParent(u,parent)
        rootY = findParent(v,parent)
        
        if rootX!=rootY:
            if rank[rootX] < rank[rootY]:
                parent[rootX] = rootY
            elif rank[rootY] < rank[rootX]:
                parent[rootY] = rootX
            else:
                parent[rootY] = rootX
                rank[rootX]+=1
            return True
        return False
    
    edges = []
    for u,v in cities:
        edges.append((u,v,c_road))
    
    mst = 0
    
    if c_road > c_lib:
        return n*c_lib
    
    parent = {i+1:i+1 for i in range(n+1)}
    rank = [0 for i in range(n+1)]
    for u,v,wt in edges:
        if findParent(u,parent)!=findParent(v,parent):
            unionbyrank(u,v,rank,parent)
            mst+=wt
    components = set()
    for i in range(1, n + 1):
        components.add(findParent(i,parent))

    # Calculate cost
    num_components = len(components)
    num_roads = len(cities)  # Not directly used in cost
    total_cost = num_components * c_lib + (n - num_components) * c_road

    return total_cost    
            
    
