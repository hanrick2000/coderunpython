class TrieNode:
    def __init__(self): 
        self.dicta={}
        self.isWord = False
            
    def addWord(self,str1):
        node = self
        for i in range(len(str1)):
            if node.dicta.get(str1[i]) == None:
                node.dicta[str1[i]] = TrieNode()
            node = node.dicta[str1[i]]
        node.isWord = True    
    
    def getNext(self,char1): 
        return self.dicta.get(char1)
    
    def isEndWord(self):
        return self.isWord
    
    def hasBegin(self,str1):
        node = self
        for i in range(len(str1)):
            if node.dicta.get(str1[i]) == None:
                return False
            node = node.dicta[str1[i]]
        return True
    
    def hasWord(self,str1):
        node = self
        for i in range(len(str1)):
            if node.dicta.get(str1[i]) == None:
                return False
            node = node.dicta[str1[i]]
        #print(str1,i,node)
        return node.isWord    
        
class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        tt = TrieNode()
        for word in words:
            tt.addWord(word)
            
        ans = set()
        str1 = []
        visited = [[ False for _ in range(len(board[0]))] for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                visited = [[ False for _ in range(len(board[0]))] for _ in range(len(board))]
                #print(visited)
                if tt.getNext(board[i][j])  == None:
                    continue
                str1.append(board[i][j])
                visited[i][j] = True
                self.dfs(board,str1,words,ans,visited,i,j,tt.getNext(board[i][j]))
                str1.pop()
        return list(ans)
        
    def dfs(self,board,str1,words,ans,visited,x,y,tt):
        #print("".join(str1))
        if tt.isEndWord():
            ans.add("".join(str1))
            
        for i,j in ([0,1],[1,0],[0,-1],[-1,0]):
            newx = x + i
            newy = y + j
            #print(x,y,board,board[0])
            if newx >=0 and newx < len(board) and newy >=0 and newy < len(board[0]) and visited[newx][newy] == False:
                if tt.getNext(board[newx][newy]) == None:
                    continue
                visited[newx][newy] = True
                str1.append(board[newx][newy])                    
                self.dfs(board,str1,words,ans,visited,newx,newy,tt.getNext(board[newx][newy]))
                str1.pop()
                visited[newx][newy] = False

if __name__ == '__main__':
    S = Solution()
    
    board = [
    ['o','a','a','n'],
    ['e','t','a','e'],
    ['i','h','k','r'],
    ['i','f','l','v']
    ]
    words = ["oath","pea","eat","rain"]
    #print(S.equalSubstring("abcd","bcdf",3))


    board = [["b","a","a","b","a","b"],["a","b","a","a","a","a"],["a","b","a","a","a","b"],["a","b","a","b","b","a"],["a","a","b","b","a","b"],["a","a","b","b","b","a"],["a","a","b","a","a","b"]]
    words = ["aab","bbaabaabaaaaabaababaaaaababb","aabbaaabaaabaabaaaaaabbaaaba","babaababbbbbbbaabaababaabaaa","bbbaaabaabbaaababababbbbbaaa","babbabbbbaabbabaaaaaabbbaaab","bbbababbbbbbbababbabbbbbabaa","babababbababaabbbbabbbbabbba","abbbbbbaabaaabaaababaabbabba","aabaabababbbbbbababbbababbaa","aabbbbabbaababaaaabababbaaba","ababaababaaabbabbaabbaabbaba","abaabbbaaaaababbbaaaaabbbaab","aabbabaabaabbabababaaabbbaab","baaabaaaabbabaaabaabababaaaa","aaabbabaaaababbabbaabbaabbaa","aaabaaaaabaabbabaabbbbaabaaa","abbaabbaaaabbaababababbaabbb","baabaababbbbaaaabaaabbababbb","aabaababbaababbaaabaabababab","abbaaabbaabaabaabbbbaabbbbbb","aaababaabbaaabbbaaabbabbabab","bbababbbabbbbabbbbabbbbbabaa","abbbaabbbaaababbbababbababba","bbbbbbbabbbababbabaabababaab","aaaababaabbbbabaaaaabaaaaabb","bbaaabbbbabbaaabbaabbabbaaba","aabaabbbbaabaabbabaabababaaa","abbababbbaababaabbababababbb","aabbbabbaaaababbbbabbababbbb","babbbaabababbbbbbbbbaabbabaa"]

    print(S.findWords(board,words))           