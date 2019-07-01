class Solution(object):
         """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        Solution: In-Place matrix operation
        Time: O(n) n is the number of elements in matrix
        Space: O(1)
        """
        length = len(matrix) - 1    # lenght of the n*n matrix, use to locate the coordinate
        h, t = 0, length            # mark the head and tail
        j = 0                       # row number
        
        while h < t:
            for i in xrange(h, t):
                matrix[i][length-j], matrix[length-j][length-i], matrix[length-i][j], matrix[j][i] = matrix[j][i], matrix[i][length-j], matrix[length-j][length-i], matrix[length-i][j]
            
            h += 1          # move to a smaller square
            t -= 1
            j += 1      
            
        return matrix
    
    
        
# You are given an n x n 2D matrix representing an image.
# Rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
