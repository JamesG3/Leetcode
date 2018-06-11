# dp solution, O(m*n)
class Solution(object):
    def uniquePaths(self, m, n):
        dp = [[0 for _ in xrange(m)] for _ in xrange(n)]
        
        dp[0] = [1 for _ in xrange(m)]
        for i in xrange(n):
            dp[i][0] = 1
            
        for i in xrange(1, n):
            for j in xrange(1, m):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]


# math solution
class Solution(object):
    def uniquePaths(self, m, n):
        return math.factorial(m+n-2)/( math.factorial(m-1) * math.factorial(n-1) )
    
    
    # using combination C(m+n-2, n-1) or C(m+n-2, m-1)
        """
        :type m: int
        :type n: int
        :rtype: int
        
        A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
        The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
        How many possible unique paths are there?
        """
        
