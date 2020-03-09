class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        self.height = len(grid)
        if not self.height:
            return 0
        self.width = len(grid[0])
        if not self.width:
            return 0
        
        islands = set()
        self.visted = set()
        self.grid = grid
        
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if n == 0 or (i, j) in self.visted:
                    continue
                    
                res = self.bfs(i, j)
                islands.add(tuple([tuple(_) for _ in res]))
        
        return len(islands)
        
        
    def bfs(self, i, j):
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        res = [[i, j]]
        
        bfs = [[i, j]]
        while bfs:
            tmp_bfs = []
            for a, b in bfs:
                self.visted.add((a, b))
                for x, y in dirs:
                    aa, bb = x + a, y + b
                    if (0 <= aa < self.height) and \
                        (0 <= bb < self.width) and \
                        self.grid[aa][bb] == 1 and \
                        (aa, bb) not in self.visted:
                        
                        tmp_bfs.append([aa, bb])
                        self.visted.add((aa, bb))
                        res.append([aa, bb])
            bfs = tmp_bfs
            
        mini, minj = min([_[0] for _ in res]), min([_[1] for _ in res])
        res = [[_[0] - mini, _[1] - minj] for _ in res]
        
        return sorted(res)
            
'''
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Solution: Hash, use relative position as the hash key
Time: O(mn)
Space: O(mn)
'''
