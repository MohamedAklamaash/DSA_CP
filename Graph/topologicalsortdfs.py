def topologicalsort(graph):
    if not graph :
        return 0
    visited = set()
    stack = []
    def dfs(graph,node):
        if node in visited:
            return
        visited.add(node)
        for neigh in graph[node]:
            if neigh not in visited:
                dfs(graph,neigh)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(graph,node)

    return stack[::-1]


