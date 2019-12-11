class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.matrix = matrix
        self.target = target
        if not self.matrix or not self.matrix[0]:
            return False
        
        self.row, self.col = len(matrix), len(matrix[0])
        vertical = False if self.row < self.col else True
        
        if vertical:
            for i in range(self.col):
                if self.binarySearch(i, True):
                    return True
        else:
            for i in range(self.row):
                if self.binarySearch(i, False):
                    return True        
        return False
        
    
        
    def binarySearch(self, i, vertical):
        s = 0
        e = self.row-1 if vertical else self.col-1
        
        while s <= e:
            m = (s + e) // 2
            cur_num = self.matrix[m][i] if vertical else self.matrix[i][m]
            if cur_num == self.target:
                return True
            
            elif cur_num < self.target:
                s = m + 1
            else:
                e = m - 1
        
        return False
    
    
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.

Solution: Binary Search on each column/row
Time: O(min(col, row) * log(max(col, row)))
Space: O(1)
'''
