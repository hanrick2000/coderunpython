def dps(node, start,end, nodeindex):
            if end<start: return False
            if start==end and node.value == voyage[start]: True
            
            if node.val != voyage[start]:
                return False
            leftstart = voyage.indexOf(node.left)
            rightstart = voyage.indexOf(node.right)
            if node.left and (leftstart == -1 or leftstart < nodeindex):
                return False
            if node.right and (rightstart == -1 or rightstart < nodeindex):
                return False
            if node.left and node.right:
                if nodeindex+1== leftstart:
                    return dps(node.right,rightstart,end) and dps(node.left,leftstart,rightstart-1)
                elif nodeindex+1== rightstart:
                    return dps(node.left,leftstart,end) and dps(node.right,rightstart,leftstart-1)
                else:
                    return False
            if node.left:
                return dps(node.left,leftstart,end)
            if node.right:
                return dps(node.right,rightstart,end)
        
        return dps(root,0,len(voyage)-1,0)