class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange_cnt = 0
        bfs = []
        visted = set()
        
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 2:
                    bfs.append([i, j])
                elif n == 1:
                    orange_cnt += 1
        if not bfs:
            return 0 if not orange_cnt else -1   
                    
        rotten_cnt = 0
        height = len(grid)
        width = len(grid[0])
        dirs = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        minute = -1
        while bfs:
            minute += 1
            tmp_bfs = []
            for i, j in bfs:
                for x, y in dirs:
                    n_i, n_j = i+x, y+j
                    if not ((0 <= n_i < height) and (0 <= n_j < width)):
                        continue
                    if grid[n_i][n_j] == 1 and (n_i, n_j) not in visted:
                        visted.add((n_i, n_j))
                        rotten_cnt += 1
                        tmp_bfs.append([n_i, n_j])
            bfs = tmp_bfs
            
        return -1 if rotten_cnt < orange_cnt else minute
            
'''
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Solution: BFS, pay attention to the description and edge cases!!!
Time, Space: O(m*n)
''' 
