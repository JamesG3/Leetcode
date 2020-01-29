class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        x_dirs = [1, 0, -1, 0]
        y_dirs = [0, 1, 0, -1]
        visted = set([])
        res = []
        
        height = len(matrix)
        if height == 0:
            return []
        
        length = len(matrix[0])
        if length == 0:
            return []
        
        dir_cnt = 0
        x, y = 0, 0
        count = 0
        while count < height * length:
            count += 1
            res.append(matrix[y][x])
            visted.add((x, y))
            dir_i = dir_cnt % 4
            
            n_x, n_y = x + x_dirs[dir_i], y + y_dirs[dir_i]
            if ((n_x, n_y) in visted) or not (0 <= n_x < length) or not  (0 <= n_y < height):
                dir_cnt += 1
                dir_i = dir_cnt % 4
                n_x, n_y = x + x_dirs[dir_i], y + y_dirs[dir_i]
            
            x, y = n_x, n_y
        return res
            
                
'''
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Solution: Simulation
Time, Space: O(mn)
'''            
            
            
        
        
