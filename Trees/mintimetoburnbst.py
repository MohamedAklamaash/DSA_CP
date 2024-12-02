from collections import deque,defaultdict

def mintimetoburstbst(root):
    if not root:
        return
    parent = {}
    def assignParents(root,par):
        if not root:
            return
        parent[root] = par
        assignParents(root.left,root)
        assignParents(root.right,root)
    assignParents(root,None)

    queue = deque([root])
    time = 0
    visited = set([root])
    while queue:
        size = len(queue)
        for _ in range(size):
            node = queue.popleft()
            for neigh in (node.left,node.right,parent[node]):
                if neigh and neigh not in visited:
                    visited.add(neigh)
                    queue.append(neigh)
        if queue:
            time+=1

    return time

