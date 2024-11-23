
from collections import deque


def toposort(graph):
    if not graph:
        return 0
    def kahnalgo(graph):
        indegree = {node:0 for node in graph}
        for node in graph:
            for neigh in graph[node]:
                indegree[neigh] = 1
        queue = deque([node for node in graph if indegree[node]==0])
        toposortarr = []
        while queue:
            node = queue.popleft()
            toposortarr.append(node)
            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return toposortarr

    if len(kahnalgo(graph)) == len(graph):
        return kahnalgo(graph)

graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': [],
}
print(toposort(graph))
