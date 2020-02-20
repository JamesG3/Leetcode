class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.height = len(matrix)
        if not self.height:
            return 0
        self.width = len(matrix[0])
        if not self.width:
            return 0
        
        
        self.dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        self.matrix = matrix
        self.visted = [[0 for _ in range(self.width)] for _ in range(self.height)]
        
        res = 0
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                res = max(res, self.dfs(i, j))
        return res
                
        
    def dfs(self, x, y):
        if self.visted[x][y] != 0:
            return self.visted[x][y]
        
        for i, j in self.dirs:
            new_x, new_y = x + i, y + j
            if (0 <= new_x < self.height and 0 <= new_y < self.width and self.matrix[new_x][new_y] > self.matrix[x][y]):
                self.visted[x][y] = max(self.visted[x][y], self.dfs(new_x, new_y))
        
        # backtracking, the largest number will have a count 1, then incremently adding to neighbors
        self.visted[x][y] += 1
        return self.visted[x][y]
        
'''
Given an integer matrix, find the length of the longest increasing path.
From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Solution: Backtracking, DFS
Time: O(n*m)
Space: O(n*m)
'''
