class Solution(object):
    def distanceK(self, root, target, k):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type k: int
        :rtype: List[int]
        """
        parent = {}
        visited = set()

        # Function to assign parents for each node
        def assignParents(node, par):
            if not node:
                return
            parent[node] = par
            assignParents(node.left, node)
            assignParents(node.right, node)
        
        # Assign parents starting from the root
        assignParents(root, None)
        res = []

        # Function to collect nodes at distance k
        def nodesAtDistK(node, dist):
            if not node or node in visited or dist > k:
                return
            visited.add(node)  # Mark the node as visited
            if dist == k:
                res.append(node.val)
                return
            nodesAtDistK(node.left, dist + 1)
            nodesAtDistK(node.right, dist + 1)
            nodesAtDistK(parent[node], dist + 1)
        
        # Start the traversal from the target node
        nodesAtDistK(target, 0)
        return res

