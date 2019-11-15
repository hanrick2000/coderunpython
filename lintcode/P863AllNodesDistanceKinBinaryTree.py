class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        def dps(root,parent=None):
            if root:
                dps(root.left,root)
                dps(root.right,root)
                root.parent = parent
        dps(root)

        q = [(target,0)]
        seen = {target}
        while q:
            if q[0][1] == K:
                return (node.val for node, dist in q)
            else:
                node, dist = q.pop(0)
                for nei in (node.left, node.right, node.parent):
                    if nei and nei not in seen:
                        q.append((nei,dist+1))
                        seen.add(nei)
        return []