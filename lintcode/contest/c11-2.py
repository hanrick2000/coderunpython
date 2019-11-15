class Solution(object):
    def transformArray(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        arr2 = arr[::]
        continueFlag = True
        while continueFlag:
            for i in range(1,len(arr)-1):
                if arr2[i] > arr2[i-1] and arr2[i] > arr2[i+1]:
                    arr[i] -= 1
                if arr2[i] < arr2[i-1] and arr2[i] < arr2[i+1]:
                    arr[i] += 1
            continueFlag = False
            for i in range(1,len(arr)-1):
                if arr[i] != arr2[i]:
                    continueFlag = True
                arr2[i] = arr[i]
        return arr2
class Solution2(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = {}
        removetimes = 0
        for e in edges:
            graph.setdefault(e[0],list()).append(e[1])
            graph.setdefault(e[1],list()).append(e[0])
        #print(graph)    
        leaves = []
        for k,v in graph.items():
            if len(v) == 1:
                leaves.append(k)
        
        while len(graph) > 2:
            new_leaves = []
            for leave in leaves:
                rem = graph[leave]
                graph[rem[0]].remove(leave)
                del graph[leave]
                if len(graph[rem[0]]) == 1:
                    new_leaves.append(rem[0])
            leaves = new_leaves
            removetimes += 1
            
        if len(graph) == 2:
            return removetimes * 2 + 1
        if len(graph) == 1:
            return removetimes * 2

if __name__ == '__main__':
    S = Solution2()
    print(S.treeDiameter([[0,1],[1,2],[2,3],[1,4],[4,5]]))
    #print(S.transformArray([6,2,3,4]))