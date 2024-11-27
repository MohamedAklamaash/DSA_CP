from collections import deque
class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        freshcount = 0
        queue = deque()
        
        # Initialize the queue with all rotten oranges and count fresh oranges
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    freshcount += 1
        
        # If no fresh oranges, return 0
        if freshcount == 0:
            return 0
        
        # BFS to spread rot
        mins = 0
        while queue:
            level_size = len(queue)
            for _ in range(level_size):  # Process all oranges in the current minute
                r, c = queue.popleft()
                for dr, dc in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = r + dr, c + dc
                    # If adjacent orange is fresh, rot it
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        freshcount -= 1
                        queue.append((nr, nc))
            
            # Only increment mins if there are more oranges to process
            if queue:
                mins += 1
        
        # If there are still fresh oranges left, return -1
        return mins if freshcount == 0 else -1

