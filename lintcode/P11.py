# Definition for a binary tree node.
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = [root]
        while q:
            pp=[]
            node = q.pop(0)
            while node:
                if not node.left and node.right: return False
                ##if not (not node.left and not node.right):
                Nochild = False
                if (not node.right) :
                    if node.left : pp.append(node.left)
                    Nochild = True
                else:
                    if (node.left or node.right) and Nochild : return False
                    if node.left : pp.append(node.left)
                    if node.right : pp.append(node.right)
                if (len(q)>0):  
                    node=q.pop(0)
                else:
                    break
            q = pp
        return True
    def isCompleteTree2(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        Nochild = False
        q = [root]
        for node in q:
            if not node.left and node.right: return False
            if (node.left or node.right) and Nochild : return False
            if (not node.right) :
                if node.left : q.append(node.left)
                Nochild = True
            else:
                if node.left : q.append(node.left)
                if node.right : q.append(node.right)
        return True
if __name__ == '__main__':
    S = Solution()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    #root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    print(S.isCompleteTree2(root))