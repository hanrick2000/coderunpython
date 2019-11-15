# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def allPossibleFBT(self, N):
        """
        :type N: int
        :rtype: List[TreeNode]
        """
        
        def helper(total):
            
            if total==1: return [TreeNode(0)]
            lefts=[]
            rights=[]
            for k in range(2,total,2):
                lefts = helper(k-1)
                rights = helper(total-k)
            re = []
            for l in lefts:
                for r in rights:
                    node = TreeNode(0)
                    node.left = l
                    node.right = r
                    re.append(node)
            return re        
        
        return helper(N)

if __name__ == '__main__':
    S = Solution()
    
    S.allPossibleFBT(7)