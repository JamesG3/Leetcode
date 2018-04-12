class Solution:
    
    # dp solution
    def findLength(self, A, B):
        lenA = len(A)
        lenB = len(B)
        dp = [[0 for _ in range(lenB+1)] for _ in range(lenA+1)]
        
        for i in range(lenA):
            for j in range(lenB):
                if A[i] == B[j]:
                    dp[i+1][j+1] = dp[i][j] + 1
                    
        return max(max(row) for row in dp)
        
        
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        
        
        # Given two integer arrays A and B, return the maximum length of an subarray that appears in both arrays.

