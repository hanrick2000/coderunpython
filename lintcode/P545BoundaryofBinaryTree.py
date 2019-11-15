#!/usr/bin/python3

import collections
from MySameTree import TreeNode

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        result = [root.val]
        if(not root.left and not root.right):
            return result
        
        curr = root.left
        if curr:
            while( curr.left or  curr.right):
                result.append(curr.val)
                if curr.left :
                    curr =  curr.left
                elif curr.right:
                    curr = curr.right
        def preorder(root):
            if not root:
                return 
            if(not root.left and not root.right):
                result.append(root.val)
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)

        preorder(root)
        
        rightboundery = []
        curr = root.right
        if curr:
            while( curr.left or  curr.right):
                rightboundery.append(curr.val)
                if curr.right :
                    curr =  curr.right
                elif curr.left:
                    curr = curr.left
        rightboundery.reverse()
        result =  result + rightboundery
        return result

if __name__ == '__main__':
    S = Solution()
    
    root = TreeNode(1)
    
    root.left = TreeNode(12) 
    root.right = TreeNode(2) 
    root.right.right = TreeNode(3) 
    root.right.left = TreeNode(4) 
    
    print(S.boundaryOfBinaryTree(root))