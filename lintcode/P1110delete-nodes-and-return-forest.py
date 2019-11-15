# Definition for a binary tree node.
from MySameTree import TreeNode;

class Solution:
    def delNodes(self, root: TreeNode, to_delete) :
        ansset = set()
        stack = []
        if root == None:
            return[]
        stack.append(root)   
        ansset.add(root)
        deleteset = set(to_delete)
        while stack:
            node = stack.pop()
            if node.val in deleteset:
                if node in ansset:
                    ansset.remove(node)
                if not node.left: ansset.add(node.left)
                if not node.right: ansset.add(node.right)

            if not node.left: stack.append(node.left)
            if not node.right: stack.append(node.right)
            
        return list(ansset)

if __name__ == '__main__':
    S = Solution()
    a = [2,3,6]
    b = [2,3,6]
    c = b
    print(a==b)
    c[1] = 1000
    print(c==b)

    #S.delNodes(root,[2,3])