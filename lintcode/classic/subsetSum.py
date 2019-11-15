class Solution:
    def subsetSum(self,arr,K):

        n = len(arr)
        if K > sum(arr):
            return False
        dp = [[False] * (K + 1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = True
        for i in range(1,n+1):
            for k in range(1,K+1):
                ans = False
                for j in range(0,i):
                    if k-arr[i-1] >= 0 :
                        ans = ans or dp[j][k-arr[i-1]] 
                    ans = ans or dp[j][k]
                    if ans:
                        break
                dp[i][k] = ans
            #print(dp)
        return dp[n][K]
                    
if __name__ == '__main__':
    S = Solution()
    

    #print(S.equalSubstring("abcd","bcdf",3))
    print(S.subsetSum([1,1,1,3,4,10],10))