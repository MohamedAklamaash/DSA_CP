from collections import deque,defaultdict

def aliendictionary(words):
    if not words:
        return []
    graph = defaultdict(list)
    for i in range(len(words)-1):
        minlen = min(len(words[i]),len(words[i+1]))
        word1 = words[i]
        word2 = words[i+1]
        if len(words[i]) > len(words[i+1]) and word1[:minlen] == word2[:minlen]:
            return []
        for j in range(minlen):
            if word1[j]!=word2[j]:
                graph[word1[j]].append(word2[j])

    def topo(graph):
        indegree = {node:0 for node in graph}
        for word in words:
            for char in word:
                indegree[char] = 0
        for node in graph:
            for neigh in graph[node]:
                indegree[neigh]+=1

        queue = deque([node for node in graph if indegree[node]==0])
        arr = []
        print(indegree)
        while queue:
            node = queue.popleft()
            arr.append(node)
            print(node)
            for neigh in graph[node]:
                indegree[neigh]-=1
                if indegree[neigh] == 0:
                    queue.append(neigh)
        return arr
    return topo(graph)
words = ["wrt", "wrf", "er", "ett", "rftt"]
print(aliendictionary(words))
