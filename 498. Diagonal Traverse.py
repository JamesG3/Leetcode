class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        height, width = len(matrix), len(matrix[0]) if matrix else 0
        if not (height and width):
            return []
        
        dir_m = [[-1, 1], [1, -1]]
        dir_m_i = 0
        res = []
        
        i, j = 0, 0
        while i < height and j < width:
            while (0 <= i < height) and (0 <= j < width):
                res.append(matrix[i][j])
                nxt_i, nxt_j = i + dir_m[dir_m_i%2][0], j + dir_m[dir_m_i%2][1]
                if not ((0 <= nxt_i < height) and (0 <= nxt_j < width)):
                    dir_m_i += 1
                    break
                i, j = nxt_i, nxt_j
            
            if i == 0 and j < width-1:
                j += 1
                
            elif j == width - 1:
                i += 1
                
            elif j == 0 and i < height - 1:
                i += 1
            
            elif i == height - 1:
                j += 1
            
        return res

    
'''
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Solution: Simulation
Time: O(mn)

'''
                
                
                
        
