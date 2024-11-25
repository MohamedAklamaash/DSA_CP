# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: Optional[TreeNode]
        """
        inorder_dict = {}
        for i,num in enumerate(inorder):
            inorder_dict[num] = i
        preiter = iter(preorder)

        def helper(start,end):
            if start > end:
                return None

            rootval = next(preiter)
            root = TreeNode(rootval)
            idx = inorder_dict[rootval]
            root.left = helper(start, idx-1)
            root.right = helper(idx+1, end)
            return root
        return helper(0,len(preorder)-1)
