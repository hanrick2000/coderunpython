class Solution(object):
    def balancedString(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s) // 4
        dicta = {}
        dicta['Q'] = 0
        dicta['W'] = 0
        dicta['E'] = 0
        dicta['R'] = 0
        for str1 in s:
            if str1 == 'Q':
                dicta['Q'] += 1
            if str1 == 'W':
                dicta['W'] += 1
            if str1 == 'E':
                dicta['E'] += 1
            if str1 == 'R':
                dicta['R'] += 1
        ans = 10000000000000
        print(dicta,n)

        for i in range(len(s)):            
            cntQ = dicta['Q'] 
            cntW = dicta['W'] 
            cntE = dicta['E'] 
            cntR = dicta['R'] 
            j = i
            while j < len(s) and (cntQ > n or cntW > n or cntE > n or cntR > n):
                if s[j] == 'Q':
                    cntQ -= 1
                if s[j] == 'W':
                    cntW -= 1
                if s[j] == 'E':
                    cntE -= 1
                if s[j] == 'R':
                    cntR -= 1
                j+=1
            #print(j,i)
            if (cntQ <= n and cntW <= n and cntE <= n and cntR <= n):
                ans = min(ans,j-i)
        return ans
if __name__ == '__main__':
    S = Solution()
    sn = S.balancedString("WWEQERQWQWWRWWERQWEQ")     # "/a/b/ca",      ,"/a/b/d"
    print(sn)    