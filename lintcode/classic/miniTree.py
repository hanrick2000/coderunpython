import collections
class Solution:
    """
    @param n: n nodes labeled from 0 to n - 1
    @param edges: a undirected graph
    @return:  a list of all the MHTs root labels
    """
    def findMinHeightTrees(self, n, edges):
        # Wirte your code here
        
        graphdict = collections.defaultdict(list)
        for edge in edges:
            graphdict[edge[0]].append(edge[1])
            graphdict[edge[1]].append(edge[0])
            
        minlevel = 10000000
        ansdict = {}
        def dfs(level,parent,node):
            children = graphdict[node]
            if len(children) == 1:
                ansdict[node] = level
                return 1
            childlevel = -1
            for child in children:
                if parent!=child:
                    childlevel = max(childlevel,dfs(level + 1,node,child))
            ansdict[node] = max(level,childlevel)
            return ansdict[node]

        leaf = None
        for key,value in graphdict.items():
            if len(value) == 1 :
                leaf = key 
                break

        ansdict[leaf] = dfs(1,leaf,graphdict[leaf][0]) + 1
        
        for key,value in ansdict.items():
            minlevel = min(minlevel,value)
        ans = []
        for key,value in ansdict.items():
            if value == minlevel:
                ans.append(key)    
        return ans

if __name__ == '__main__':
    S = Solution()
    print(S.findMinHeightTrees(6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]))  #(4,[[1,0],[1,2],[1,3]]))