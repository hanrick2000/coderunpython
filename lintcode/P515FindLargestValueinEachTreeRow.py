#!/usr/bin/python3

import collections
from MySameTree import TreeNode;
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.levelvalue = []

        def visit(root,level):
            if not root:
                return 
            if self.levelvalue[] < root.levelvalue:
                self.levelvalue[level] = root.levelvalue
            if root.left:
                visit(root.left,level+1)
            if root.right:
                visit(root.right.level+1)
            return
        
        visit(root,0)
        return self.levelvalue