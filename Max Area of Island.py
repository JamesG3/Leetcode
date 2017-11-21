class Solution(object):
    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        
        def dfsHelper(i, j):
            if 0<=i<m and 0<=j<n and grid[i][j]==1:
                grid[i][j] = 0
                return 1 + dfsHelper(i-1, j) + dfsHelper(i+1, j) + dfsHelper(i, j-1) + dfsHelper(i, j+1)
            return 0
        
        maxArea = 0
        for i in xrange(m):
            for j in xrange(n):
                if grid[i][j]:
                    maxArea = max(dfsHelper(i,j), maxArea)
        return maxArea
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) 
        # You may assume all four edges of the grid are surrounded by water.
        # Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)
