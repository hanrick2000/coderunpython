import collections
import queue
class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        dict={}
        for i in range(len(s)):
            cnt = dict.get(s[i],0)
            dict.set(s[i],cnt+1)
            if ((cnt+1) % 2) == 0:
                totallen = cnt + 1
            else:
                totallen -= cnt
                maxji = max(maxji,cnt+1)
        return totallen + maxji

class Solution2:
    """
    @param source: 
    @param target: 
    @return: return the index
    """
    def strStr(self, source, target):
        BASE = 1000000
        # Write your code here
        power = 1
        m = len(target)
        for i in range(len(target)):
            power = (power *31 ) % BASE
        targetHash = 0
        for i in range(len(target)):
            targetHash = (targetHash * 31 + ord(target[i])) % BASE
        hashValue=0
        for i in range(len(source)):
            ##abc + d
            hashValue = (hashValue * 31 + ord(source[i])) % BASE
            if i<m-1:
                continue
            if i>=m:
                hashValue -= (ord(source[i-m]) * power) % BASE
                if hashValue<0:
                    hashValue += BASE
            #print(source[i-m+1:i+1])
            if hashValue ==  targetHash and source[i-m+1:i+1]==target:
                return i-m+1
        return -1



class Solution3:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        if s==None or len(s)==0:
            return True
        left =  0
        right = len(s) - 1
        
        # write your code here
        while(left<right):
            
            if not leftchar.isalnum():
                left+=1
            elif not rightchar.isalnum():
                right-=1
            elif leftchar.lower() != rightchar.lower():
                return False
            else:
                left+=1
                right+=1

        return True


    def rotateString(self, s, offset):
            # write your code here
        if s==None or len(s) == 0:
            return s
        items = s
        offset = offset % len(s)
        def rotateOne(items):
            temp = items[len(s)-1]
            for i in range(len(s)-2,-1,-1):
                items[i+1]=items[i]
            items[0] = temp
            return items

        for i in range(offset):
            items = rotateOne(items)
        
class Solution5:
    def numIslands(self, grid):
        
        
        def bfs(row,col,grid):
            stack = collections.deque()
            stack.append((row,col))
            while stack:
                point = stack.popleft()
                
                if(point[0]-1>-1 and grid[point[0]-1][point[1]]=="1"):
                    stack.append((point[0]-1,point[1]))
                    grid[point[0]-1][point[1]] = "-1"
                    
                if( point[0]+1<len(grid) and grid[point[0]+1][point[1]]=="1"):
                    stack.append((point[0]+1,point[1]))
                    grid[point[0]+1][point[1]] = "-1"
                    
                if(point[1]-1>-1 and grid[point[0]][point[1]-1]=="1"):
                    stack.append((point[0],point[1]-1))
                    grid[point[0]][point[1]-1] = "-1"
                    
                if(point[1]+1<len(grid[0]) and grid[point[0]][point[1]+1]=="1"):
                    stack.append((point[0],point[1]+1))
                    grid[point[0]][point[1]+1] = "-1"
                #print(stack)
        if grid ==None or len(grid)==0 or len(grid[0])==0:
            return 0
        islandsCnt = 0
        # write your code here
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    grid[row][col] = "-1"
                    bfs(row,col,grid)
                    islandsCnt +=1
        return islandsCnt    
class Solution615:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        if not prerequisites and numCourses>=0:
            return True
        # write your code here
        depends = {}
        for i in range(numCourses):
            depends[i] = set()
        for course, precourse in prerequisites:
            depends.setdefault(course, set()).add(precourse)
            
        
        queue = collections.deque()
        for course, precourses in depends.items():
            if len(precourses) == 0:
                queue.append(course)
        
        processedcnt = 0
        while queue:
            #print(queue)
            nodevalue = queue.popleft()
            processedcnt += 1
            for course, precourses in depends.items():
                if nodevalue in precourses:
                    precourses.remove(nodevalue)
                    if len(precourses) == 0:
                        queue.append(course)
        #print(processedcnt)
        return numCourses == processedcnt

class Solution108:
    def minCut(self, s):
        if s == None or len(s)==0 :return -1
        if len(s)==1 : return 0
        def isPalindrome(s,start,end):
            while start<=end:
                if s[start] != s[end]:
                    return False
                start += 1 
                end -= 1
            return True
        
        queue1 = queue.Queue()
        queue1.put([0,0])
        
        jumped = set()
        while queue1: 
            node = queue1.get()    
            print(node)       
            start = node[0]
            step = node[1]
            if start >= len(s): 
                ans = step - 1
                break
            
            for i in range(start,len(s)):
                if i+1 in jumped : continue
                if isPalindrome(s,start, i ):
                    queue1.put((i+1,step+1))
                    jumped.add(i+1)
           
        return ans

    def minCutTimeout(self, s):
        if s == None or len(s)==0 :return -1
        if len(s)==1 : return 0
        def isPalindrome(s,start,end):
            while start<=end:
                if s[start] != s[end]:
                    return False
                start += 1 
                end -= 1
            return True
        # write your code here
        biggestp = collections.defaultdict(list)
        for i in range(len(s)):
            for k in range(i,len(s)):
                if isPalindrome(s,i,k):
                    biggestp[i].append(k+1)
        print(biggestp)
        queue = collections.deque()
        queue.append(0)
        level = 0
        jumped = set()
        while queue:
            nextq = collections.deque()
            while queue:
                node = queue.popleft()
                for n in biggestp[node]:
                    if n == len(s): return level
                    if not n in jumped:
                        nextq.append(n)
                        jumped.add(n)
            queue = nextq
            level += 1
        return level
    def minCutFailed(self, s):
            if s == None or len(s)==0 :return -1
            if len(s)==1 : return 0
            def isPalindrome(s,start,end):
                while start<=end:
                    if s[start] != s[end]:
                        return False
                    start += 1 
                    end -= 1
                return True
            
            queue1 = collections.deque()
            queue1.append([0,0])
            
            jumped = set()
            while queue1: 
                #print(queue1)
                node = queue1.popleft()           
                start = node[0]
                step = node[1]
                if start >= len(s): 
                    ans = step - 1
                    break
                
                for i in range(start,len(s)):
                    if i+1 in jumped : continue
                    if isPalindrome(s,start, i):
                        queue1.append((i+1,step+1))
                        jumped.add(i+1)
            
            return ans
    def ladderLength(self, start, end, dict1):
     # write your code here
        def isOneDiff(a,b):
            if len(a)!=len(b): return False
            k = 0
            for i in range(len(a)):
                if a[i]!=b[i]:
                    k +=1 
                    if k>1: return False
            return k == 1
        if start == end: return 1
        if len(dict1) == 0 or len(start)!=len(end): return 0
        
        
        queue = collections.deque()
        queue.append(start)
        
        reached = set()
        level = 2
        while queue:
            p = collections.deque()
            while queue:
                fromstr = queue.popleft()
                if isOneDiff(fromstr,end): return level
                for d in dict1:
                    if (d not in reached) and isOneDiff(d,fromstr):
                        p.append(d)
                        reached.add(d)
            level+=1 
            queue = p
class Solution447:
    """
    @param: reader: An instance of ArrayReader.
    @param: target: An integer
    @return: An integer which is the first index of target.
    """
    def searchBigSortedArray(self, reader, target):
       
        index = 1 
        while True:
            if reader.get(index) == 2147483647:
                break;
            if reader.get(index) >= target:
                break;
            index = index * 10 
        
        left = 0 
        right = index 
        while left>=right:
            mid = left + (right - left) // 2 
            if s.get(mid) > target:
                right = mid - 1 
            elif s.get(mid) < target:
                left = mid + 1
            else:
                return mid 
        return -1
a = [["1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","0","1","0","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","0"],["1","0","1","1","1","0","0","1","1","0","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","0","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","0","1","1","1","1","1","1","0","1","1","1","0","1","1","1","0","1","1","1"],["0","1","1","1","1","1","1","1","1","1","1","1","0","1","1","0","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","1","1"],["1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["0","1","1","1","1","1","1","1","0","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","0","1","1","1","1","1","1","1","0","1","1","1","1","1","1"],["1","0","1","1","1","1","1","0","1","1","1","0","1","1","1","1","0","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","1","1","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","0","1","1","1","1","0","0"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"],["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","1"]]
if __name__ == '__main__':
    s2 = Solution108()
    #print(s2.minCut("1111aaz2aa1111ddd"))
    #print(s2.minCutFailed("1111aaz2aa1111ddd"))
    #print(s2.minCutFailed("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"))
    s3 = Solution447()
    s3.searchBigSortedArray()