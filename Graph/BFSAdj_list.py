from collections import defaultdict, deque

def bfs(start, graph: dict):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    print("BFS Traversal Order:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        visited.add(node)
        for neigh in graph[node]:
            if neigh not in visited:
                queue.append(neigh)

def main():
    graph = defaultdict(list)
    graph[0].extend([1, 2])
    graph[1].extend([2])
    graph[2].extend([0, 3])
    graph[3].extend([3])

    start_node = 2
    bfs(start_node, graph)

if __name__ == "__main__":
    main()


