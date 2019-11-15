class Solution:
    def getMaximumGold(self, grid):
        ans = 0
        
        visited = set()
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 0: 
                    continue
                re = self.dfs(x,y,grid,visited)
                ans = max(ans,re)
                
        return ans
        
    def dfs(self,x,y,grid,visited):
        
        stepans = 0
        visited.add((x,y))
        for dir in [[0,1],[1,0],[-1,0],[0,-1]]:
            newx = x + dir[0]
            newy = y + dir[1]     
            if newx < 0 or newx >= len(grid) or newy < 0  or newy >= len(grid[0]) or grid[newx][newy] == 0 or (newx,newy) in visited:
                continue                      
            re = self.dfs(newx,newy,grid,visited) 
            #print(newx,newy,re,visited)
            stepans = max(re,stepans)

        visited.remove((x,y))
        return stepans + grid[x][y]
        

if __name__ == '__main__':
    S = Solution()
    

    #print(S.equalSubstring("abcd","bcdf",3))
    print(S.getMaximumGold([[0,6,0],[5,8,7],[0,9,0]]))