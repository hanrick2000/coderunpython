class Solution(object):
    def criticalConnectionsMy(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        graph = {}
        for con in connections:
            graph.setdefault(con[0],list()).append(con[1])
            graph.setdefault(con[1],list()).append(con[0])
        #print(graph)
        def remove(edges,fromnode,selfpath,selfnode):
            if fromnode not in selfnode:
                return
            for i in range(len(selfpath)-1,-1,-1):
                if (selfpath[i][0],selfpath[i][1]) in edges:
                    edges.remove((selfpath[i][0],selfpath[i][1]))
                if (selfpath[i][1],selfpath[i][0]) in edges:
                    edges.remove((selfpath[i][1],selfpath[i][0]))
                if selfpath[i][0] == fromnode:
                    break
                    
        def add(path,edge):
            #print(path,edge)
            if (edge[0],edge[1]) not in path and (edge[1],edge[0]) not in path:
                path.add((edge[0],edge[1]))
                
        def dfs(fromnode,parent,visited,path,selfpath,selfnode):
            for node in graph[parent]:                
                if node == fromnode:
                    continue
                if node not in visited:
                    #print(parent,node,path)
                    visited.add(node)
                    add(path,[parent,node])
                    selfnode.add(node)
                    #print(path)
                    selfpath.append((parent,node))
                    dfs(parent,node,visited,path,selfpath,selfnode)
                    selfnode.remove(node)
                    selfpath.pop()
                else:
                    remove(path,node,selfpath,selfnode)
        visited = set()
        visited.add(connections[0][0])
        ans = set()
        selfnode = set()
        selfnode.add(connections[0][0])
        dfs(None,connections[0][0],visited,ans,[],selfnode)
        return ans



    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        self.Rank = [None]*n
        self.Graph = [[] for i in range(n)]
        self.result = []
        self.color = [0]*n
        self.level = [0]*n
        for [node1, node2] in connections:
            self.Graph[node1].append(node2)
            self.Graph[node2].append(node1)

        self.DFS(0, None)
        return self.result

    def DFS(self, node, parent):
        self.color[node] = 1
        if parent == None:
            level = 0
        else:
            level = self.level[parent] + 1

        self.level[node] = level
        self.Rank[node] = level

        for child in self.Graph[node]:
            if child == parent:
                continue
            if self.color[child] == 0:
                self.DFS(child, node)
                if self.Rank[child] < self.Rank[node]:
                    self.Rank[node] = self.Rank[child]

                if self.level[node] < self.Rank[child]:
                    self.result.append([node, child])

            elif self.color[child] == 1:
                if self.Rank[node] > self.level[child]:
                    self.Rank[node] = self.level[child]

        self.color[node] = 2
class Solution2:
    # @param {integer[]} preorder
    # @return {boolean}
    def verifyPreorder(self, preorder):
        low = float("-inf")
        path = []
        for p in preorder:
            if p < low:
                return False
            while path and p > path[-1]:
                low = path[-1]
                path.pop()
            path.append(p)
        return True

if __name__ == '__main__':
    S = Solution2()
    root = [5,2,1,3,6,4]
    sn = S.verifyPreorder(root)
    #sn = S.criticalConnections(6,[[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]])
    print(sn)   