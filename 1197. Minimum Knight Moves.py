class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        dirs = [[2, 1], [1, 2], [-1, 2], [-2, 1], [-1, -2], [2, -1], [-2, -1], [1, -2]]
        visted = set([(0, 0)])
        
        if (x, y) == (0, 0):
            return 0
        
        bfs = [[0, 0]]
        count = 0
        while bfs:
            tmp_bfs = []
            count += 1
            for i, j in bfs:
                for di, dj in dirs:
                    ni, nj = i + di, j + dj
                    if (ni, nj) not in visted:
                        if (ni, nj) == (x, y):
                            return count
                        visted.add((ni, nj))
                        tmp_bfs.append([ni, nj])
            bfs = tmp_bfs
        
                        
'''
In an infinite chess board with coordinates from -infinity to +infinity, you have a knight at square [0, 0].
A knight has 8 possible moves it can make, as illustrated below. Each move is two squares in a cardinal direction, then one square in an orthogonal direction.

Solution: BFS, Hashset
'''       
        
        
        
