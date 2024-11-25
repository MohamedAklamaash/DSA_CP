# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorderdict = {val:i for i,val in enumerate(inorder)}

        def helper(start, end):
            if start > end:
                return None
            root = TreeNode(postorder.pop())
            idx = inorderdict[root.val]
            root.right = helper(idx+1, end)
            root.left = helper(start, idx -1)
            return root
        return helper(0,len(postorder)-1)
