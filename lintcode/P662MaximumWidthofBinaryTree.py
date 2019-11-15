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
    def widthOfBinaryTreeBFS(self, root):
    
            q = [(root,0,0)]
            cur_level =left= ans = 0
            
            for node,level,pos in q:
                if node:
                    q.append(node.left,level+1,2*pos)
                    q.append(node.right,level+1,2*pos+1)
                    if cur_level!=level:
                        cur_level = level
                        left = pos
                    ans = max(ans,pos-left+1)

            return ans

    def widthOfBinaryTreeDFS(self, root):
    
            self.ans = 0
            startdict = {}
            def dfs(node, level = 0, pos = 0):
                if node:
                    startdict.setdefault(level,pos)
                    ans = max(ans,pos-startdict[level]+1)
                    dfs(node.left,level+1,2*pos)
                    dfs(node.right,level+1,2*pos+1)
            dfs(root)
            return self.ans 
