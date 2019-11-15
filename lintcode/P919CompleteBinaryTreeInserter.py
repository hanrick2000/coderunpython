#!/usr/bin/python3

import collections
from MySameTree import TreeNode;
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.que = collections.deque()
        self.root = root
        q = [root]
        for node in q:
            if not node.left and not node.right:
                self.que.append(node)
            else:
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            


    def insert(self, v):
        """
        :type v: int
        :rtype: int
        """
        node = self.que.popleft()
        if not node.left:
            node.left = TreeNode(v)
            self.que.appendleft(node)
        elif not node.right:
            node.right = TreeNode(v)
        return node

        
    def get_root(self):
        """
        :rtype: TreeNode
        """
        return self.root

if __name__ == '__main__':
    root = TreeNode(1)
    
    root.left = TreeNode(2) 
    root.right = TreeNode(3) 
    root.left.left = TreeNode(4) 
    root.left.right = TreeNode(5) 
    root.right.left = TreeNode(6) 
    obj = CBTInserter(root)
    param_1 = obj.insert(1)
    param_1 = obj.insert(2)
    param_1 = obj.insert(3)
    param_1 = obj.insert(4)
    param_1 = obj.insert(5)
    param_1 = obj.insert(6)
    param_2 = obj.get_root()
# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(v)
# param_2 = obj.get_root()