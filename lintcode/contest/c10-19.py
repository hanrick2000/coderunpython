import collections
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def leftViewUtil(self,root):    # root above   
        if root == None:
            return []
        queue = collections.deque() 
        queue.append(root) #1
        ans = [] 
        while len(queue)!=0: # 1 1 2
            isFirst = True 
            tmp = len(queue)  #1 1 2 2
            for _ in range(tmp): # looptimes1 1 2 2
                node = queue.popleft() # q=[]1 []3 [7]6 [2]7 [8]2 []8
                if isFirst:  
                    isFirst = False 
                    ans.append(node.data) # [1] [1,3] [1,3,6] [1,3,6,2]
                if node.left:
                    queue.append(node.left) #  [] [6] [7] [2] [8] []
                if node.right:
                    queue.append(node.right) # [3] [6,7] [7,2] [2,8] [8] []
                
        return ans


            
if __name__ == '__main__':
    S = TreeNode(1)
    root = TreeNode(2)
    root.left = TreeNode(10)
    root.right = TreeNode(2)
    root.right.left = TreeNode(21)
    print(root.leftViewUtil(root))
    #sn = S.removeSubfolders(["/ah/al/am","/ah/al"])     # "/a/b/ca",      ,"/a/b/d"
    #print(sn)