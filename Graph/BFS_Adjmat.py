from collections import deque

def bfs(start, graph):
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    print("BFS Traversal Order:")
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        # vertex,edge
        for neighbor, connected in enumerate(graph[node]):
            if connected and neighbor not in visited:  # Check if there is an edge and if not visited
                visited.add(neighbor)
                queue.append(neighbor)

def main():
    # Define an adjacency matrix for the graph
    graph = [
        [0, 1, 1, 0],  # Node 0 is connected to 1 and 2
        [0, 0, 1, 1],  # Node 1 is connected to 2 and 3
        [1, 0, 0, 1],  # Node 2 is connected to 0 and 3
        [0, 0, 0, 1]   # Node 3 is connected to itself (loop)
    ]
    
    # Start BFS traversal from node 2
    start_node = 2
    bfs(start_node, graph)

if __name__ == "__main__":
    main()

