from collections import deque,defaultdict

def mintimetoburstbst(root,target):
    if not root or not target:
        return
    parent = {}
    def assignParents(root,par):
        if not root:
            return
        parent[root] = par
        assignParents(root.left,root)
        assignParents(root.right,root)
    assignParents(root,None)

    queue = deque([target])
    time = 0
    visited = set([target])
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

