class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def all_traversals(root):
    if not root:
        return [], [], []

    stack = [(root, 1)]  # Stack contains tuples of (node, state)
    preorder, inorder, postorder = [], [], []

    while stack:
        node, state = stack.pop()

        if state == 1:  # Preorder
            preorder.append(node.value)
            stack.append((node, 2))  # Update state to 2 for the same node
            if node.left:
                stack.append((node.left, 1))  # Push the left child with state 1
        elif state == 2:  # Inorder
            inorder.append(node.value)
            stack.append((node, 3))  # Update state to 3 for the same node
            if node.right:
                stack.append((node.right, 1))  # Push the right child with state 1
        elif state == 3:  # Postorder
            postorder.append(node.value)  # Process for postorder

    return preorder, inorder, postorder
# Example usage:
# Construct the binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

preorder, inorder, postorder = all_traversals(root)
print("Preorder:", preorder)    # Output: [1, 2, 4, 5, 3]
print("Inorder:", inorder)      # Output: [4, 2, 5, 1, 3]
print("Postorder:", postorder)  # Output: [4, 5, 2, 3, 1]

