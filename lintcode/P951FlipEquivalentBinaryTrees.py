#!/usr/bin/python3

import collections
from MySameTree import TreeNode;
class Solution(object):
    def flipEquiv(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        if root1 is root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        return (self.flipEquiv(root1.left,root2.left) and 
                self.flipEquiv(root1.right,root2.right)) or (
                self.flipEquiv(root1.left,root2.right) and 
                self.flipEquiv(root1.right,root2.left)
                )
        

if __name__ == '__main__':
    S = Solution()
    
    root = TreeNode(5)
    root.left = TreeNode(2) 
    root.right = TreeNode(3) 
    root.right.right = TreeNode(4) 
    root2 = TreeNode(5)
    root2.right = TreeNode(2) 
    root2.left = TreeNode(3) 
    root2.left.right = TreeNode(4) 
    print(S.flipEquiv(root,root2))