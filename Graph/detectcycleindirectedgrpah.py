from collections import deque

def detectcycleindirgraph(graph,visited,pathvisited):
    
    def dfs(graph,node):
        visited[node] = 1
        pathvisited[node] = 1

        for neigh in graph[node]:
            if visited[node] == 0:
                if dfs(graph,neigh):
                    return True
            elif pathvisited[node]:
                return True
        pathvisited[node] = 0
        return False

    for node in range(len(graph)):
        if dfs(graph,node) and visited[node] == 0:
            return True
    
    return False


