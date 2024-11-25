# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def findPath(node, path, target):
            if not node:
                return False
            path.append(node)  # Store the actual node, not just its value
            if node == target:
                return True
            if findPath(node.left, path, target) or findPath(node.right, path, target):
                return True
            path.pop()
            return False

        path1, path2 = [], []
        findPath(root, path1, p)
        findPath(root, path2, q)
        
        lca = None
        for u, v in zip(path1, path2):
            if u == v:
                lca = u
        
        return lca
