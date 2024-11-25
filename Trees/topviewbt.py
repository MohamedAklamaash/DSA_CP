def topView(root):
    if not root:
        return
    
    # Dictionary to store the first node at each horizontal distance
    hd_node_map = {}
    
    # Queue for level-order traversal, storing pairs of (node, horizontal distance)
    queue = [(root, 0)]
    
    while queue:
        node, hd = queue.pop(0)
        
        # If this is the first node at this horizontal distance, add it
        if hd not in hd_node_map:
            hd_node_map[hd] = node.info
        
        # Add left and right children to the queue
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Extract the top view nodes in order of horizontal distance
    for hd in sorted(hd_node_map.keys()):
        print(hd_node_map[hd], end=" ")

