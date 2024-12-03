
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def swapNodes(indexes, queries):
    inorderres = []
    
    # Function for in-order traversal
    def inorder(root):
        if not root:
            return
        inorder(root.left)
        inorderres.append(root.val)
        inorder(root.right)
    
    # Build the tree from the indexes input
    n = len(indexes)
    nodes = {i + 1: TreeNode(i + 1) for i in range(n)}  # Create nodes 1 to n
    
    for i, (left, right) in enumerate(indexes, start=1):
        nodes[i].left = nodes[left] if left != -1 else None
        nodes[i].right = nodes[right] if right != -1 else None
    
    # Function to swap subtrees at a given depth
    def swap_subtrees_at_depth(root, depth, k):
        if not root:
            return
        if depth % k == 0:
            root.left, root.right = root.right, root.left  # Swap the children
        swap_subtrees_at_depth(root.left, depth + 1, k)
        swap_subtrees_at_depth(root.right, depth + 1, k)
    
    # Perform the swap operations based on the queries
    result = []
    for k in queries:
        # Perform the swap at the given depth k
        swap_subtrees_at_depth(nodes[1], 1, k)
        
        # Reset inorder traversal result for this query
        inorderres = []
        inorder(nodes[1])  # Perform the in-order traversal
        result.append(inorderres)
    
    return result

# Example Input
indexes = [
    (2, 3),  # Node 1: left -> 2, right -> 3
    (-1, -1), # Node 2: left -> None, right -> None
    (-1, -1)  # Node 3: left -> None, right -> None
]
queries = [2]  # Query to swap subtrees at depth 2

# Calling the function
print(swapNodes(indexes, queries))  # Expected Output: [[3, 1, 2]]

