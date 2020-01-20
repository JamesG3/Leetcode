class Solution(object):
    # Math solution
    def numTrees(self, n):
        # Catalan Number  (2n)! / ((n+1)! * n!) 
        return math.factorial(2*n) / (math.factorial(n+1)*math.factorial(n))
                
    # DP solution    
    def numTrees(self, n: int) -> int:
        dp = [0 for _ in range(n+1)]
        dp[0] = 1
        
        # for each node as the root
        for i in range(1, n+1):
            # sum of dp[left_sub] * dp[right_sub] for each combination(length) of subtrees
            for j in range(1, i+1):
                dp[i] += dp[i-j] * dp[j-1]
        return dp[-1]
    
'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Time: DP - O(n^2), Math - O(n)
Space: DP - O(n), Math - O(1)
'''
        
        
