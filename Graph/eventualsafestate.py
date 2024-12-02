class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        
        visited = {}

        def dfs(node):
            if node in visited:
                return visited[node]
            visited[node] = True
            for neigh in graph[node]:
                if dfs(neigh):
                    return True
            visited[node] = False
        res = []
        for i in range(len(graph)):
            if not dfs(i):
                res.append(i)
        res.sort()
        return res

if __name__ == "__main__":
    test_graphs = [
        ([[1, 2], [2, 3], [5], [0], [5], [], []], [2, 4, 5, 6]),  # Safe nodes: [2, 4, 5, 6]
        ([[1, 2], [2, 3], [3], [4], [0]], []),  # Cycle present, no safe nodes
        ([[], [0], [1, 2], [1]], [0, 1, 2, 3]),  # All nodes are safe
        ([[], [2], [3], [4], []], [0, 1, 2, 3, 4]),  # All nodes are safe
        ([[], [], [], []], [0, 1, 2, 3]),  # Empty graph
    ]

    for idx, (graph, expected) in enumerate(test_graphs):
        result = Solution().eventualSafeNodes(graph)
        print(f"Test Case {idx + 1}: {'Pass' if result == expected else 'Fail'}")
