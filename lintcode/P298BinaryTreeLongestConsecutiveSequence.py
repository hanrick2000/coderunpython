# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#!/usr/bin/python3
from MySameTree import TreeNode;
class Solution:
    def longestConsecutive(self, root: TreeNode) -> int:
        self.cnt = 0
        self.helper(root,1)
        return self.cnt
    def helper(self, root: TreeNode,parentCnt):
        if root==None :
            return
        if root.left!=None:
            if(root.left.val > root.val):
                parentCnt +=1
                self.cnt = max(self.cnt,parentCnt)
                self.helper(root.left,parentCnt)
            else:
                self.helper(root.left,1)
        if root.right!=None:
            if(root.right.val > root.val):
                parentCnt +=1
                self.cnt = max(self.cnt,parentCnt)
                self.helper(root.right,parentCnt)
            else:
                self.helper(root.right,1)
if __name__ == '__main__':
    S = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2) 
    root.right = TreeNode(4)
    root.left.left = TreeNode(6)
    print(S.longestConsecutive(root))