import collections
import sys
class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        queue = collections.deque()
        dis = [[sys.maxsize for _ in range(len(maze[0]))] for _ in range(len(maze))]
        dis[start[0]][start[1]] = 0
        queue.append((start[0],start[1]))
        while queue:
            x,y = queue.popleft()
            for i,j in [(0,1),(0,-1),(1,0),(-1,0)]:
                newx = x + i
                newy = y + j
                adis = 0
                while newx >= 0 and newx < len(maze) and newy >= 0 and newy < len(maze[0]) and maze[newx][newy] != 1: 
                    newx = newx + i
                    newy = newy + j
                    adis += 1
                if dis[x][y] + adis < dis[newx - i][newy - j]:
                    dis[newx - i][newy - j] = dis[x][y] + adis
                    queue.append((newx - i, newy - j))

        return -1 if dis[destination[0]][destination[1]] == sys.maxsize else dis[destination[0]][destination[1]]

if __name__ == '__main__':
    S = Solution()
    sn = S.shortestDistance([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],[0,4],[4,4])     # "/a/b/ca",      ,"/a/b/d"
    print(sn)   