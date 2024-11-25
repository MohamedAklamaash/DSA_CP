from collections import defaultdict, deque
def verticalordertraversal(root):
    if not root:
        return []
    lvls = defaultdict(list)
    queue = deque([(root,0)])
    while queue:
        node,lvl = queue.popleft()
        lvls[lvl].append(node.data)
        if node.left:
            queue.append((node.left,lvl-1))
        if node.right:
            queue.append((node.right,lvl+1))
    res = []
    for key in sorted(list(lvls.keys())):
        vals = lvls[key]
        res.append(vals)
    return res


