import math
class Solution:
    def cutBamboo(self, bamboo):
        bamboo.sort() #2 2 4 4 5 6 8
        ans = []
        for i in range(len(bamboo)): 
            j = i
            if bamboo[i] == 0:
                continue
            cuts = 0
            cutb = bamboo[i]
            while j < len(bamboo):
                bamboo[j] -= cutb
                cuts += 1
                j += 1
                #print(bamboo)
            ans.append(cuts)
        return ans

    def findfactors(self,n,k):
        factorset = set()
        for i in range(1,int(math.sqrt(n)) + 1):
            if n % i == 0:
                factorset.add(n//i)
                factorset.add(i)
        factors = list(factorset)
        factors.sort()
        return factors[k-1] if k-1 < len(factors) else 0

    def mathWork(self,thredhold,arr):
        days = 0
        for i in range(1,len(arr)):
            if arr[i] - arr[0] >= thredhold:
                days = i
                break
        if days == 0:
            return len(arr)
        else:
            if days % 2 == 0:
                return days
            else:
                return days // 2 + 1

if __name__ == '__main__':
    S = Solution()
    #print(S.cutBamboo([2]))  #1,2,3,4
    print(S.findfactors(20,3))
    print(S.findfactors(20,6))
    print(S.findfactors(20,12))