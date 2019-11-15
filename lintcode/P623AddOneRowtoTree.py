#!/usr/bin/python3
from MySameTree import TreeNode;
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if not root:
            return
        level = 0
        q = [root]
        if d==1:
            t = root
            root = TreeNode(v)
            root.left = t
            return root
        z = []
        while q:
            level+=1
            if level == d-1 :
                z=z+q 
            p=[]
            for node in q:     
                for leaf in (node.left, node.right):
                    #print leaf.val
                    if leaf:
                        p.append(leaf)
            q=p
        
                
        if level+1 == d:
            for n in z:
                n.left = TreeNode(v)
                n.right = TreeNode(v)
        else:
            for change in z:
                if change.left:
                    t = change.left
                    change.left = TreeNode(v)
                    change.left.left  =  t
                if change.right:
                    t = change.right
                    change.right = TreeNode(v)
                    change.right.right  =  t
        return root

if __name__ == '__main__':
    S = Solution()
    
    root = TreeNode(4)
    
    root.left = TreeNode(2) 
    root.right = TreeNode(6) 
    root.left.left = TreeNode(3) 
    root.left.right = TreeNode(1) 
    root.right.left = TreeNode(5) 
    z=[1,2,]
    p=z
    z.insert(0,1)
    z=[]
    for n1 in p:
        print(n1)
    print("----------")
    for n1 in z:
        print(n1)
    #print(S.addOneRow(root,1,3))