class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        max_area = 0
        height = len(matrix)
        if not height:
            return max_area
        
        width = len(matrix[0])
        if not width:
            return max_area
        
        matrix = [[int(_) for _ in row] for row in matrix]
        
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if i == 0 or j == 0:
                    max_area = max(max_area, n)
                    continue
                    
                if n != 1:
                    continue
                
                # expand the square by checking the 3 neighbor nodes
                exist_square = min(matrix[i][j-1], matrix[i-1][j], matrix[i-1][j-1])
                matrix[i][j] = exist_square + 1
                max_area = max(max_area, matrix[i][j] ** 2)
                
        return max_area
                    
        
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Solution: DP
Time: O(nm)
Space: O(nm), extra O(1)
'''

