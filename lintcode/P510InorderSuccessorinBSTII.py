#!/usr/bin/python3
from MySameTree import TreeNode;
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, parent):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent
"""
class Solution(object):
    def inorderSuccessor(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        def minValue(root):
            if not root.left and not root.right:
                return root
            if root.left:
                return minValue(root.left)
            if root.right:
                return minValue(root.right)
        def upperParent(root):
            if not root.parent :
                return None
            if root.parent.left == root:
                return root.parent
            return upperParent(root.parent)

        if node.right:
            return minValue(node.right)    
        else:
            return upperParent(node)
