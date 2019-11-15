class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """
    def kSumII(self, A, k, target):
        # write your code here
        def dfs(start,aim,midresult,result,cnt):
            if aim == 0:
                result.append(midresult[::])
                return
            
            if cnt == 0:
                return
            
            for i in range(start,len(A)):
                if A[i] > aim:
                    break
                midresult.append(A[i])
                dfs(i+1,aim-A[i],midresult,result,cnt-1)
                midresult.pop()
        
        A.sort()
        ans = []
        dfs(0,target,[],ans,k)
        return ans

if __name__ == '__main__':
    S = Solution()
    print(S.kSumII([1,2,3,4],2,5))