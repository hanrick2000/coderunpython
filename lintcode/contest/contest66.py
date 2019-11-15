import heapq
class Solution:
    """
    @param m: an integer
    @param n: an integer
    @param N: an integer
    @param i: an integer
    @param j: an integer
    @return: the number of paths to move the ball out of grid boundary
    """
    def findPaths(self, m, n, N, i, j):
        
        # Write your code here
        a = self.dfs(m,n,N,i,j,{})  % (10 ** 9 + 7)
        return a  

    def dfs(self,m,n,N,i,j,memo):
        if (N,i,j) in memo:
            return memo[(N,i,j)]
        if N==0:
            return 0
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        stepsum = 0
        for d in directions:
            x = i + d[0] 
            y = j + d[1] 
            if x > m - 1 or x < 0 or y > n - 1 or y < 0 :
                stepsum += 1
            else:
                stepsum += self.dfs(m,n,N-1,x,y,memo)
        memo[(N,i,j)] = stepsum
        return stepsum

    def test_headq(self):
        pq = []
        heapq.heappush(pq, (0, 100))
        heapq.heappush(pq, (1, 21))
        heapq.heappush(pq, (2, 11))
        heapq.heappush(pq, (0, 11))
        heapq.heappush(pq, (1, 1))
        while pq:
            move = heapq.heappop(pq)
            print(move)
        
if __name__ == '__main__':
    s2 = Solution()
    #print(s2.findPaths(2,2,12,0,1))
    s2.test_headq()