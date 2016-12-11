class Solution(object):
    def setZeroes(self, matrix):
        if len(matrix)==0:              #if empty, return nothing
            return
        
        x=[]                #saving the coordinate of 0
        y=[]                #saving the coordinate of 0
        
        
        for i, row in enumerate(matrix):            #traversal the matrix and find the 0's coordinate
            for j, element in enumerate(row):
                if element==0:
                    if i not in y:
                        y.append(i)
                    if j not in x:
                        x.append(j)
        
        
        for i in y:                         #time-saving replace, replace the elements directly
            matrix[i]=[0]*len(matrix[0])
            
        for j in x:
            counter=0
            while counter != len(matrix):
                matrix[counter][j]=0
                counter+=1
        
        """         
        #brute force replace:
        
        for i in xrange(len(matrix)):
            for j in xrange(len(matrix[0])):
                if i in y or j in x:
                    matrix[i][j]=0
                    
                
        
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        
        
        #Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
