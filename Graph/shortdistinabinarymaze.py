import heapq

def shortpathinabinarymaze_with_path(adjmat, srcrow, srccol, destrow, destcol):
    """
    Finds the shortest path and its length in a binary maze from (srcrow, srccol) to (destrow, destcol).
    
    :param adjmat: List[List[int]], binary matrix where 1 indicates walkable and 0 indicates wall
    :param srcrow: int, source row
    :param srccol: int, source column
    :param destrow: int, destination row
    :param destcol: int, destination column
    :return: tuple (distance, path), where path is a list of (row, col) positions or (-1, []) if unreachable
    """
    if not adjmat or not adjmat[0]:
        return -1, []

    rows, cols = len(adjmat), len(adjmat[0])

    # Check for invalid input positions
    if (
        srcrow < 0 or srcrow >= rows or srccol < 0 or srccol >= cols or
        destrow < 0 or destrow >= rows or destcol < 0 or destcol >= cols
    ):
        return -1, []

    # Check if source or destination is a wall
    if adjmat[srcrow][srccol] == 0 or adjmat[destrow][destcol] == 0:
        return -1, []

    # Initialize distance matrix and parent tracking
    distance = [[float("inf") for _ in range(cols)] for _ in range(rows)]
    distance[srcrow][srccol] = 0
    parent = { (srcrow, srccol): None }  # To trace the path

    # Priority queue for Dijkstra's algorithm
    pq = [(0, srcrow, srccol)]  # (distance, row, col)

    # Define possible movements (up, down, left, right)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while pq:
        curr_dist, curr_row, curr_col = heapq.heappop(pq)

        # If we reach the destination
        if curr_row == destrow and curr_col == destcol:
            # Trace back the path
            path = []
            node = (curr_row, curr_col)
            while node:
                path.append(node)
                if node not in parent:  # Debug: Ensure valid key
                    print(f"Error: {node} not found in parent.")
                    return -1, []
                node = parent[node]
            return curr_dist, path[::-1]  # Return distance and reversed path

        # Skip if the current cell has already been processed with a shorter distance
        if curr_dist > distance[curr_row][curr_col]:
            continue

        # Explore neighbors
        for dr, dc in directions:
            new_row, new_col = curr_row + dr, curr_col + dc

            # Check for valid neighbors
            if 0 <= new_row < rows and 0 <= new_col < cols and adjmat[new_row][new_col] == 1:
                new_dist = curr_dist + 1  # Each step has a weight of 1
                if new_dist < distance[new_row][new_col]:
                    distance[new_row][new_col] = new_dist
                    parent[(new_row, new_col)] = (curr_row, curr_col)  # Update parent
                    heapq.heappush(pq, (new_dist, new_row, new_col))

    # If destination is not reachable
    return -1, []

# Example Debugging Case
maze = [
    [1, 0, 0, 1],
    [1, 1, 0, 1],
    [0, 1, 1, 1],
    [0, 0, 1, 1]
]
src_row, src_col = 0, 0
dest_row, dest_col = 3, 3

distance, path = shortpathinabinarymaze_with_path(maze, src_row, src_col, dest_row, dest_col)
print(f"Distance: {distance}")
print(f"Path: {path}")

