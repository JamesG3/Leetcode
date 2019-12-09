class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # check if either m/n is 0
        h = len(matrix)
        if not h:
            return False
        
        w = len(matrix[0])
        if not w:
            return False
        
        # binary search to find the target row
        h1, h2 = 0, h
        while h1 < h2:
            h_m = (h1 + h2) // 2
            if matrix[h_m][-1] < target:
                h1 = h_m + 1
            elif matrix[h_m][-1] > target:
                if matrix[h_m][0] > target:
                    h2 = h_m
                elif matrix[h_m][0] < target:
                    break
                else:
                    return True
            else:
                return True
        
        # target row not found
        if not (h1 < h2):
            return False
        
        # binary search to find the target in the target row
        target_row = matrix[h_m]
        r1, r2 = 0, len(target_row)
        while r1 < r2:
            r_m = (r1 + r2) // 2
            if target_row[r_m] > target:
                r2 = r_m
            elif target_row[r_m] < target:
                r1 = r_m + 1
            else:
                return True
            
        return False
                
'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Solution: binary search
Time: O(log(m) + log(n))
Space: O(1)
'''     
