# dp solution
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n = len(obstacleGrid[0]), len(obstacleGrid)
        dp = [[0 for _ in xrange(m)] for _ in xrange(n)]
        
        for i in xrange(n):
            for j in xrange(m):
                if obstacleGrid[i][j] != 0:
                    continue
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
                    
        return dp[-1][-1]
               
        
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        
        # A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
        # The robot can only move either down or right at any point in time. 
        # The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
        # Now consider if some obstacles are added to the grids. How many unique paths would there be?
        # For example, the input matrix would be:
        #        [
        #  [0,0,0],
        #  [0,1,0],
        #  [0,0,0]
        #        ]
