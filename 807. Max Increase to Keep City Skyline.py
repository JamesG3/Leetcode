class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        Solution: Find max for lines and rows, compare and calculate sum of diff
        Time: O(n)
        Space: O(n)
        """
        if not grid:
            return grid
        
        Y = len(grid)
        X = len(grid[0])
        
        y_max = [max(r) for r in grid]
        x_max = []
        for x in xrange(X):
            cur_max = 0
            for y in xrange(Y):
                cur_max = max(cur_max, grid[y][x])
            
            x_max.append(cur_max)
            
            
        res = 0
        for y in xrange(Y):
            for x in xrange(X):
                res += min(y_max[y], x_max[x]) - grid[y][x]
            
        return res
        
        
        # pythonic solution
        row_max = [max(row) for row in grid]
        col_max = [max(col) for col in zip(*grid)]
        
        return sum(min(row_max[r], col_max[c]) - val for r, row in enumerate(grid) for c, val in enumerate(row))
            
                
