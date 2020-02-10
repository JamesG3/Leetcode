class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]] 
        k, j, dir_i = 0, 0, 0
        
        for i in range(n**2):
            matrix[k][j] = i+1
            x, y = dirs[dir_i % 4]
            tmp_k, tmp_j = k + x, j + y
            if (tmp_k >= n or tmp_j >= n) or matrix[tmp_k][tmp_j] != 0:
                dir_i += 1
                x, y = dirs[dir_i % 4]
                k, j = k + x, j + y
            else:
                k, j = tmp_k, tmp_j
        
        return matrix


'''
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Solution: Simulation, list
Time, Space: O(n**2)
'''        
                
        
