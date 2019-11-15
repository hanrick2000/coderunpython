#Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
 
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p is None and q is None:
            return True
        if p is None or q is None or p.val !=q.val:
            return False
        return self.isSameTree(p.left, q.left)and self.isSameTree(p.right, q.right)
 
           
if __name__ == '__main__':
    S = Solution()
    l1 = TreeNode(4)
    l2 = TreeNode(2)
    l3 = TreeNode(6)
    l4 = TreeNode(1)
    l5 = TreeNode(5)
    l6 = TreeNode(3)
    l7 = TreeNode(7)
      
    root = l1
   
    l1.left = l2
    l1.right = l3
   
    l2.left = l4
    l2.right = l5
    l3.left = l6
    l3.right = l7

    S.isSameTree(root,l1)