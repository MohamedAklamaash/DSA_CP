
def iterativePreorder(root):
    if not root:
        return None
    s = []
    res = []
    s.append(root)
    while s:
        node = s.pop()
        res.append(node.val)
        if node.right:
            s.append(node.right)
        if node.left:
            s.append(node.left)
    return res

def iterativeInorder(root):
    if not root:
        return []
    stack = []
    node = root
    inorder = []
    while True:
        if node!=None:
            stack.append(node)
            node = node.left
        else:
            if len(stack) == 0:
                break
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
    return inorder

def iterativePostOrder(root):
    if not root:
        return []
    s1 = [root]
    s2 = []
    while s1:
        node = s1.pop()
        s2.append(node)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    arr = []
    while s2:
        node = s2.pop()
        arr.append(node.val)
    return arr

