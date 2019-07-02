class Solution(object):
    def __init__(self):
        self.traversed = set()
        
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        Solution: Union find
        Time: O(n*m)
        Space: O(n*m)
        """
        if not grid:
            return 0
        self.grid = grid
        self.height = len(grid)
        self.length = len(grid[0])
        res = 0
        
        for j in xrange(self.height):
            for i in xrange(self.length):
                if self.grid[j][i] == "1":
                    if (j, i) in self.traversed:
                        continue
                    
                    self.find(i, j)
                    res += 1
        return res
        
        
    
    def find(self, i, j):
        if (j, i) in self.traversed:
            return
        
        if self.grid[j][i] == "1":
            self.traversed.add((j, i))
            if i+1 < self.length:
                self.find(i+1, j)
            if i-1 > -1:
                self.find(i-1, j)
            if j+1 < self.height:
                self.find(i, j+1)
            if j-1 > -1:
                self.find(i, j-1)
        else:
            return
            
        
# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
#You may assume all four edges of the grid are all surrounded by water.       
