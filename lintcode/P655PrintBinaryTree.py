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
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root :
            return None
        q=[root]
        
        dicta = collections.defaultdict(list)
        dicta[0] = [root]
        level = 0
        while q:
            p=[]
            isNone = True
            for node in q :
                if not node:
                    p.append(None)
                    p.append(None)
                else:
                    for leaf in (node.left, node.right):
                        if leaf:
                            isNone = False
                        p.append(leaf)
            if not isNone:
                level+=1
                dicta[level] = p
                q = p
            else:
                break
        
        result = []
        elecnt = (2*len(q))-1
        j = 0
        levelpos=[]
        while j<=elecnt:
            levelpos.append(j)
            j+=2
        for l in range(level,-1,-1):
            i = 0
            k = 0
            r = []
            for i in range(0,elecnt):
                if i in levelpos:
                    r.append(dicta[l][k].val if dicta[l][k] else "")
                    k+=1
                else:
                    r.append("")
            result.insert(0,r)
            j = 0
            levelpos2=[]
            while j<len(levelpos) and len(levelpos)>1:
                levelpos2.append((levelpos[j]+levelpos[j+1])//2)
                j+=2
            levelpos = levelpos2
        return result
if __name__ == '__main__':
    S = Solution()
    
    root = TreeNode(5)
    root.left = TreeNode(2) 
    root.right = TreeNode(3) 
    root.right.right = TreeNode(3) 
    print(S.printTree(root))