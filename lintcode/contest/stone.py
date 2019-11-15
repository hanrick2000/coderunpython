class Solution:
    def lastStoneWeightII(self, stones):
        used = [False for _ in range(len(stones))]
        self.ans = 1000000
        stones.sort()
        self.dfs(stones,used,len(stones))

        return self.ans
        
    def dfs(self,stones,used,leftcnt):
        if leftcnt == 0:
            self.ans = 0
            return 0
        if leftcnt == 1:
            for i in range(len(used)):
                if used[i] == False:
                    self.ans = min(stones[i],self.ans)
                    return
        start = 0
        for i in range(len(stones)):
            if used[i] == False:
                start = i
                break
        for i in range(start + 1,len(stones)):
            if used[i] == False:
                if stones[i] == stones[start]:
                    used[i] = True
                    used[start] = True    
                    starttmp = stones[start]
                    curtmp = stones[i]
                    stones[start] = 0
                    stones[i] = 0            
                    if self.dfs(stones,used,leftcnt - 2)  == 0 :
                        return 0
                    stones[start] = starttmp
                    stones[i] = curtmp 
                    used[i] = False
                    used[start] = False
                else:
                    used[i] = False
                    used[start] =  True
                    starttmp = stones[start]
                    curtmp = stones[i]
                    stones[i] = abs(stones[i] - stones[start])  
                    stones[start] = 0                   
                    if self.dfs(stones,used,leftcnt - 1) == 0:
                        return 0
                    stones[start] = starttmp
                    stones[i] = curtmp 
                    used[i] = False
                    used[start] = False
        
                
if __name__ == '__main__':
    S = Solution()
    

    #print(S.equalSubstring("abcd","bcdf",3))
    print(S.lastStoneWeightII([1,1,2,3,5,8,13,21,34,55,89,14,23,37,61,98]))