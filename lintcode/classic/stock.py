class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        trans = 3
        dp = [[[0 for _ in range(2)] for _ in range(trans) ] for _ in range(len(prices) )]
        if trans > len(prices)/2 :
            sum = 0
            for i in range(1,len(prices)):
                if prices[i] - prices[i-1] > 0:
                    sum += prices[i] - prices[i-1]
            return sum
            
        for i in range(len(prices)):
            for k in range(trans):   #0 sell #1 buy
                if i==0:
                    dp[i][k][1] = -prices[i]
                    continue
                if k==0:
                    dp[i][k][0] = max(dp[i-1][k][1] + prices[i],dp[i-1][k][0])
                    dp[i][k][1] = max( - prices[i],dp[i-1][k][1])
                    continue                
                dp[i][k][0] = max(dp[i-1][k][1] + prices[i],dp[i-1][k][0])
                dp[i][k][1] = max(dp[i-1][k-1][0] - prices[i],dp[i-1][k][1])
        #print(dp)        
        return dp[len(prices)-1][trans-1][0]

if __name__ == '__main__':
    S = Solution()
    

    #print(S.equalSubstring("abcd","bcdf",3))
    print(S.maxProfit([2,3,4,9]))        