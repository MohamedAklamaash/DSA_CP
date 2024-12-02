from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        # Queue stores pairs of (node, index)
        queue = deque([(root, 1)])
        max_width = 0
        
        while queue:
            level_length = len(queue)
            _, first_index = queue[0]  # First node's index in the level
            for _ in range(level_length):
                node, index = queue.popleft()
                # Append children with their respective indices
                if node.left:
                    queue.append((node.left, 2 * index))
                if node.right:
                    queue.append((node.right, 2 * index + 1))
            
            # Last node's index in the level
            _, last_index = queue[-1] if queue else (None, 0)
            # Update max_width
            max_width = max(max_width, last_index - first_index + 1)
        
        return max_width

