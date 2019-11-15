# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    cnt = 0
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        #print(root.val)
        if (root==None) :
            return 0
        self.subTree(root)
        return self.cnt
    def subTree(self, root: TreeNode) :
        
        if(root.left == None and root.right == None):
            self.cnt += 1
            return True
        else:
            lbe = False
            rbe = False
            if (root.left != None):
                lbe = self.subTree(root.left)
            if (root.right != None):
                rbe = self.subTree(root.right)
            if(((lbe and root.left.val==root.val) or root.left ==None) and ((rbe and root.right.val == root.val) or root.right==None)):
                self.cnt += 1
                return True
            else:
                return False 
        
if __name__ == '__main__':
    S = Solution()
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    print(S.countUnivalSubtrees(None))