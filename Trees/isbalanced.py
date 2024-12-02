class Solution:
    def isBalanced(self, root) -> bool:
        def height(root):
            if not root:
                return 0
            
            left_height = height(root.left)
            right_height = height(root.right)
            
            if left_height == -1 or right_height == -1:
                return -1
            
            if abs(left_height - right_height) > 1:
                return -1
            
            return max(left_height, right_height) + 1
        
        return height(root) != -1
