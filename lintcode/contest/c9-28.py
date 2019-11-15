class Solution1:
    def uniqueOccurrences(self, arr) :
        dict1 = {}
        dict2 = {}
        for a in arr:
            dict1[a]=dict1.setdefault(a,0) + 1
            
        for value in dict1.values():
            if dict2.setdefault(value,0) != 0:
                return False            
            dict2[value] = 1
            
        return True

class Solution2:
    def equalSubstring(self, s, t, maxCost):
        if maxCost == 0:
            return 1
        dis = []
        dis.append(0)
        for i in range(len(s)):
            dis.append(abs(ord(s[i]) - ord(t[i])))
        ans = 0
        k = 0
        j = 0
        for i in range(1, len(dis)):
            k = k - dis[i-1]
            print(i,j,k)
            while k <= maxCost and j < len(dis) -1:
                j +=1
                k += dis[j]
                print("----",i,j,k)
            if j == len(dis)-1 and k <= maxCost:
                ans = max(ans,j-i+1)
            else:
                ans = max(ans,j-i)
        return ans

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if k==1:
            return ""
        stack1 = []
        stack2 = []
        for char in s:
            stack1.append(char)
        found = True
        while found:
            found = False
            same = 1
            while stack1:
                node = stack1.pop()
                if len(stack2)>0 and node == stack2[-1]:
                    same += 1
                    if same == k:
                        found = True
                        for _ in range(k-1):
                            stack2.pop()
                    else:
                        stack2.append(node)
                else:
                    same = 1
                    stack2.append(node)
            stack2 = stack2[::-1]
            stack1, stack2 = stack2, stack1
        return ''.join(stack1) if len(stack1)>0 else ''.join(stack2)

if __name__ == '__main__':
    S = Solution()
    

    #print(S.equalSubstring("abcd","bcdf",3))
    print(S.removeDuplicates("abcd",2))