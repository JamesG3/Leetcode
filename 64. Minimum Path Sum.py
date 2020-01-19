class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        height, width = len(grid), len(grid[0])
        
        for i, row in enumerate(grid):
            for j, n in enumerate(row):
                if i == 0:
                    if j == 0:
                        continue
                    grid[i][j] += grid[i][j-1] 
                    continue
                
                if j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                    
        return grid[-1][-1]

'''
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
Note: You can only move either down or right at any point in time.

Solution: DP, compare two parent paths, update the current node with shorter path
Time: O(n)
'''
