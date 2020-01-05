class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        visted = set()
        height = len(matrix)
        width = len(matrix[0])
        
        dfs = []
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if n == 0:
                    dfs.append([i, j])
        
        dist = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        while dfs:
            dist += 1
            tmp_dfs = []
            for i, j in dfs:
                for dir_x, dir_y in dirs:
                    m, n = i + dir_x, j + dir_y
                    if (0 <= m < height) and (0 <= n < width) and (m, n) not in visted:
                        if matrix[m][n] == 0:
                            continue
                            
                        visted.add((m, n))
                        tmp_dfs.append([m, n])
                        matrix[m][n] = dist
            dfs = tmp_dfs
        return matrix
                        
'''
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Solution: DFS
Time, Space: O(n)
'''        
                    
        
        
