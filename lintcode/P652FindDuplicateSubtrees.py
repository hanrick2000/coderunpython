#!/usr/bin/python3
from MySameTree import TreeNode;
import collections;
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        tempsame =[]
        def helper(q):
            isLeaf = True
            p=[]
            self.tempsame = []
            for node in q:
                if node:
                    if node.left:
                        p.append(node.left)
                        isLeaf = False
                    if node.right:
                        p.append(node.right)
                        isLeaf = False
            if isLeaf:              
                sameset =[]
                mm = q
                while mm:
                    node = mm.pop()
                    for node2 in q:
                        if node2.val == node.val :
                            if len(sameset) == 0:
                                sameset.append(node)
                            sameset.append(node2)
                            mm.remove(node2)
                        

                    self.sameall.append(sameset)
                    self.tempsame.append(sameset)
                return
            else:
                helper(p)
                
            upsameall = []
            upsameset = []
            for sameset in self.tempsame:
                for node in q:
                    if (node.left in sameset and node.right in sameset):
                        upsameset += [node]
                if len(upsameset)>1:
                    self.sameall.append(upsamset[0])
                    upsameall.append(upsameset)
            self.tempsame = upsameall
            
        self.sameall = []
        helper([root])
        return self.sameall

    def findDuplicateSubtreesIndentify(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        trees = collections.defaultdict()
        trees.default_factory = trees.__len__
        count = collections.Counter()        
        ans = []
        def lookup(node):
            if node:
                uid = trees[node.val, lookup(node.left),lookup(node.right)]
                count[uid]+=1
                if count[uid]==2:
                    ans.append(node)
                return uid
        lookup(root)
        return ans
    def findDuplicateSubtreesSerial(self, root):
        count = collections.Counter()
        ans=[]
        def helper(root):
            if root:
                if not root.left:
                    le = '#'
                else:
                    le = helper(root.left)
                
                if not root.right:
                    ri = '#'
                else:
                    ri = helper(root.right)

                sresult = le + str(root.val) + ri
                count[sresult] +=1
                if count[sresult] == 2:
                    ans.append(root)
                return sresult
            else:
                return '#'


if __name__ == '__main__':
    S = Solution()
    
    root = TreeNode(1)
    
    root.left = TreeNode(2) 
    root.right = TreeNode(3) 
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.left.left = TreeNode(4)
    #root.right.right = TreeNode(3) 
    #root.right.left = TreeNode(4) 
    
    print(S.findDuplicateSubtreesSerial(root))