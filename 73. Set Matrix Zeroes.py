class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # use this var to mark if the first col need to be updated to all 0
        is_col = False
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                # bypass the first column, use is_col to remember
                if j == 0:
                    if n == 0:
                        is_col = True
                    continue
                
                # if a number is 0, update the most top element & the most left element to 0
                if n == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0
        
        # bypass the first col and row, traverse the rest, 
        # if the most top || most left element is 0, update the current to 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                    
        # if the upper left coner is 0, the row should be all 0
        if matrix[0][0] == 0:
            matrix[0] = [0 for _ in matrix[0]]
        
        # if we ever updated this var, means the whole col should be all 0
        if is_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0
                
                

'''
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.
Could you devise a constant space solution?

Solution: In-place, divide and conquer, DP, optimization
Time: O(mn)
Space: O(1)
'''
