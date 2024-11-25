
def isLeaf(node):
    if not node:
        return False
    if node.left and node.right:
        return True
    return False

def left(node,boundary):
    if not node:
        return
    while node:
        if not isLeaf(node):
            boundary.append(node.data)
        node = node.left if node.left else node.right

def right(node,boundary):
    temp = []
    if not node:
        return
    while node:
        if not isLeaf(node):
            temp.append(node.data)
        node = node.right if node.right else node.left

    boundary.extend(temp[::-1])

def leaf(node,boundary):
    if not node:
        return
    if isLeaf(node):
        boundary.append(node.data)
    leaf(node.left,boundary)
    leaf(node.right,boundary)

def boundaryTraversal(root):
    if not root:
        return []
    boundary = []
    if not isLeaf(root):
        boundary.append(root.data)
    left(root.left,boundary)
    leaf(root,boundary)
    right(root.right,boundary)
