#!/usr/bin/python3
from MySameTree import TreeNode;
class Codec:
    def serialize1(self, root):
        """
        Encodes a tree to a single string.
        """
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return ' '.join(map(str, postorder(root)))

    def deserialize1(self, data):
        """
        Decodes your encoded data to tree.
        """
        def helper(lower = float('-inf'), upper = float('inf')):
            if not data or data[-1] < lower or data[-1] > upper:
                return None
            
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root
        
        data = [int(x) for x in data.split(' ') if x]
        return helper()

    def serialize(self, root):
        """
        Encodes a tree to a single string.
        """
        def postorder(root):
            return postorder(root.left) + postorder(root.right) + [root.val] if root else []
        return ' '.join(map(str,postorder(root)))

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        """
        def helper(lower=float('-inf'), higher = float('inf')):           
            if not data or data[-1] < lower or data[-1] > higher:
                return None
            val = data.pop()
            root = TreeNode(val)
            root.right = helper(val,higher)
            root.left = helper(lower,val)
            return root

        data = [int(x) for x in data.split(' ') if x]
        return helper()
if __name__ == '__main__':
    S = Codec();
    root = TreeNode(1)
    root.left = TreeNode(2) 
    root.right = TreeNode(4)
    root.left.left = TreeNode(6)
    bincom = S.serialize(root)
    print(bincom)
    a = S.deserialize(bincom)
    print(a.val)