#!/usr/bin/python3
from MySameTree import TreeNode;
import sys
import collections
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        freq = collections.defaultdict(int)

        def dps(root):
            if not root:
                return 0
            if not root.left and not root.right:
                freq[root.val] += 1
                return root.val
            val = root.val
            val += dps(root.left)
            val += dps(root.right)
            freq[val]+=1
            return val
        dps(root)

        r = sorted(freq.items(),key =lambda p:p[1],reverse=True)
        return [ k for k,v in r if v == r[0][1]]

    def test(self):
        d = {'art': 'van gogh', 'opera': 'carmen'}            # Set value in current context
        #d['x']                # Get first key in the chain of contexts
        #del d['x']            # Delete from current context
        #list(d)               # All nested values
        #k in d                # Check all nested values

        '''
        print(len(d))                # Number of nested values
        print(d.items())             # All nested items
        for k in d.items():
            print(k)
        '''
if __name__ == '__main__':
    S = Solution()
    
    root = TreeNode(5)
    root.left = TreeNode(2) 
    root.right = TreeNode(-3)
    #root.left.left = TreeNode(10)
    print(S.findFrequentTreeSum(root))