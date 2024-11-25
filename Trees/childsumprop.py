# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def changeTree(self, root):
        """
        :type root: TreeNode
        :rtype: None
        Modifies the tree in-place to satisfy the Children Sum Property.
        """
        if not root:
            return

        # Recursively adjust left and right subtrees
        self.changeTree(root.left)
        self.changeTree(root.right)

        # Calculate the sum of child nodes
        left_val = root.left.val if root.left else 0
        right_val = root.right.val if root.right else 0
        child_sum = left_val + right_val

        # If node value is less than child sum, update node value
        if child_sum > root.val:
            root.val = child_sum
        # If node value is greater than child sum, propagate excess to children
        elif child_sum < root.val:
            diff = root.val - child_sum
            if root.left:
                root.left.val += diff
            elif root.right:
                root.right.val += diff
            
            # Ensure children satisfy the property after propagation
            if root.left:
                self.changeTree(root.left)
            if root.right:
                self.changeTree(root.right)

