class Solution(object):
    def rotate(self, matrix):
        l=len(matrix)-1                 #lenght of the n*n matrix, use to locate the coordinate
        start=0                         #mark the range of a matrix
        end=l-1                         #mark the range of a matrix
                                        #substitute the coordinate from the outside square
        while start <= end:
            for n in range(start,end+1):
                matrix[start][n], matrix[n][l-start], matrix[l-start][l-n], matrix[l-n][start] = matrix[l-n][start], matrix[start][n], matrix[n][l-start], matrix[l-start][l-n]
            start+=1                    #move to a smaller square and substitute every coordinate
            end-=1
            
        
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        
        You are given an n x n 2D matrix representing an image.
        Rotate the image by 90 degrees (clockwise).
        
        Requirement: Could you do this in-place?
        """
        
