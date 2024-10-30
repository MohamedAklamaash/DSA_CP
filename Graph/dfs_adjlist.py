from collections import defaultdict
from typing import Dict

def dfs(node,graph,visited):
    visited.add(node)
    print(node,end=' ')
    for neigh in graph[node]:
        if neigh not in visited:
            dfs(neigh,graph,visited)

def main():
    # Define the graph using an adjacency list
    graph = defaultdict(list)
    graph[0].extend([1, 2])
    graph[1].extend([2])
    graph[2].extend([0, 3])
    graph[3].extend([3])

    # Start DFS traversal from node 2
    start_node = 2
    visited = set()  # Set to keep track of visited nodes
    print("DFS Traversal Order:")
    dfs(start_node, graph, visited)

if __name__ == "__main__":
    main()
