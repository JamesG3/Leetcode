class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix) == 0  or len(matrix[0]) == 0:
            return False
        
        i = len(matrix[0])-1            # from the largest number of the first line
        for row in matrix:              # move to a larger number
            while i>0 and row[i] > target:  # if not out of range & larger  ->   move to a smaller one
                i -= 1
            if row[i] == target:
                return True
        return False
                
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        # time: O(m+n)
        
        
        # Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
        # Integers in each row are sorted in ascending from left to right.
        # Integers in each column are sorted in ascending from top to bottom.
