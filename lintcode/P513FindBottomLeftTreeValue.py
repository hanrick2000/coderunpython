#!/usr/bin/python3
from MySameTree import TreeNode;
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxLevel = 0
        self.maxValue = 0

        def dfs(root,level):
            if not root:
                return
            if level > self.maxLevel:
                self.maxLevel = level
                self.maxValue = root.val
            dfs(root.left,level+1)
            dfs(root.right, level +1)
            return

        dfs(root,1)
        
        return self.maxValue