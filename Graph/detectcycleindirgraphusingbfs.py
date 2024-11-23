from collections import deque

def detectcycle(graph):
    if not graph:
        return 0
    
    def kahn(graph):
        indegree = {node:0 for node in graph}
        for node in graph:
            for neigh in graph[node]:
                indegree[neigh]+=1

        queue = deque([node for node in graph if indegree[node]==0])
        arr = []
        while queue:
            node = queue.popleft()
            arr.append(node)
            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return arr

    if(len(kahn(graph)) != len(graph)):
        return True
    return False




