class Solution(object):
    def isToeplitzMatrix(self, matrix):
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if i == 0 or j == 0:
                    continue
                if n != matrix[i-1][j-1]:
                    return False
        return True
        
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        
        
        
        # A matrix is Toeplitz if every diagonal from top-left to bottom-right has the same element.
        # Now given an M x N matrix, return True if and only if the matrix is Toeplitz.
