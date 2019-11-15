class Solution:
    """
    @param source: the input string
    @return: the number of subsequences 
    """
    def countSubsequences(self, source):
        # write your code here
        blist = []
        
        # first B 
        acnt, ccnt = 0,0
        foundB = False
        firstbindex = 0
        for i in range(len(source)):
            if source[i] == "a" and not foundB:
                acnt += 1
            if source[i] == "b" and not foundB:
                foundB = True
                firstbindex = i
            if foundB and source[i] == "c":
                ccnt += 1
        blist.append((acnt,ccnt))
        #print("------------",blist) 

        for i in range(firstbindex+1,len(source)):
            if source[i] == "a" and i > firstbindex :
                acnt += 1
            if source[i] == "b":
                blist.append((acnt,ccnt))
            if source[i] == "c" and i > firstbindex:
                ccnt -= 1
        print(blist)     

        ans = 0

        for i in range(len(blist)):
            for j in range(i,len(blist)):
                beforea = blist[i][0]
                afterc = blist[j][1]
                if i != j:
                    tmp = self.rangeR(beforea, afterc) * pow(2,(j-i)-1)
                else:
                    tmp = self.rangeR(beforea, afterc) 
                print(tmp)
                ans += tmp
        return ans
        
    def combine(self,n):
        return pow(2,n) - 1
        
    def rangeR(self,start,end):
        return self.combine(start) * self.combine(end)
        
                        
if __name__ == '__main__':
    S = Solution()
    import numpy as np
    def triple_var_by_ref(x):
        x[0]=x[0]*3
    a=np.array([2])
    triple_var_by_ref(a)
    print(a+1)

    #print(S.equalSubstring("abcd","bcdf",3))
    #print(S.countSubsequences("abbbbbbc")) #abacbbcc
        
        
        
        