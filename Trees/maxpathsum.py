# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        maxi = [float("-inf")]
        def helper(root):
            if not root:
                return 0
            left = max(helper(root.left),0)
            right = max(helper(root.right),0)
            maxi[0] = max(maxi[0],root.val+left+right)
            return root.val + max(left,right)
        helper(root)
        return maxi[0]
