#!/usr/bin/python3
#from sys import List
#: List[int]
import sys
class Solution:
    def verifyPreorder2(self, preorder) -> bool:
        return self.helper(preorder,0,len(preorder))
    def helper(self, preorder,startp,endp) -> bool:
        if(startp >= endp-1):
            return True
        mid = startp
        for i in range (startp+1,endp):
            if(preorder[i] < preorder[startp]):
                mid = i
            else:
                break
        
        if mid < endp:
            for i in range (mid+1,endp):
                if(preorder[i] < preorder[startp]):
                    return False
        if not self.helper(preorder,startp+1,mid+1):
            return False
        if not self.helper(preorder,mid+1,endp):
            return False
        #print(str(mid)+" "+str(preorder[mid]))

        return True

    def verifyPreorder(self, preorder):
            """
            :type preorder: List[int]
            :rtype: bool
            """
            stk = []
            root = -sys.maxsize-1
            for val in preorder:
                if val<root:
                    return False
                
                while stk and stk[-1]<val:
                    root = stk.pop()
                
                stk.append(val)
                
            return True
if __name__ == '__main__':
    S = Solution()
    print(S.verifyPreorder([5,2,1,3,6]))