def dfs(node, graph, visited):
    print(node, end=' ') 
    visited.add(node)
    for vertex, edge in enumerate(graph[node]):
        if edge and vertex not in visited:
            dfs(vertex, graph, visited)  # Corrected to call dfs with vertex

def main():
    # Define an adjacency matrix for the graph
    graph = [
        [0, 1, 1, 0],  # Node 0 is connected to 1 and 2
        [0, 0, 1, 1],  # Node 1 is connected to 2 and 3
        [1, 0, 0, 1],  # Node 2 is connected to 0 and 3
        [0, 0, 0, 1]   # Node 3 is connected to itself (loop)
    ]
    
    # Start DFS traversal from node 2
    start_node = 2
    visited = set()  # Set to keep track of visited nodes
    print("DFS Traversal Order:")
    dfs(start_node, graph, visited)

if __name__ == "__main__":
    main()

