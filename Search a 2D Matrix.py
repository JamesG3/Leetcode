class Solution(object):
    def searchMatrix(self, matrix, target):
        if len(matrix)==0:                    #check if matrix is empty
            return False
        if target in matrix[0]:               #check the first list in matrix
            return True
        
        right=len(matrix)                     #initialize the value of right, left and mid
        left=0
        mid=len(matrix)/2
        
        while mid != right and mid != left:   #binary search
            if target<matrix[mid][0]:
                right=mid
                mid=mid/2
                
            elif target>=matrix[mid][0] and target<=matrix[mid][-1]:
                if target in matrix[mid]:
                    return True
                else:
                    return False
            else:
                left=mid
                mid=(mid+right)/2
        return False
                
            
        
        """
        Because the matrix is sorted
        So we can use binary search
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        
        Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
        Integers in each row are sorted from left to right.
        The first integer of each row is greater than the last integer of the previous row.
        """
        
