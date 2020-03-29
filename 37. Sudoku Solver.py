class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.empty = []
        # get all empty slots saved into a list, will traverse and backtracking base on this list
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                if n == '.':
                    self.empty.append([i, j])    
        self.helper(0)
        
    # recursive backtracking function
    def helper(self, empty_i):
        # when we finish the traversal of self.empty, means there is a solution found
        if empty_i == len(self.empty):
            return True
        
        i, j = self.empty[empty_i]
        candis = self.find_candis(i, j)
        # deadend, need to return
        if not candis:
            return False
        
        # try to replace self.board[i][j] with each candidate
        for n in candis:
            self.board[i][j] = n
            if not self.helper(empty_i+1):
                continue
            else:
                return True
        # if all candidates are failed to proceed, revert change on self.board[i][j], return False, go back to previous level
        self.board[i][j] = '.'
        return False
                
    # check row, column, cell, return the rest of candidates can be used
    def find_candis(self, i, j):
        candis = set('123456789')
        for x in range(9):
            n = self.board[x][j]
            m = self.board[i][x]
            if n != '.' and n in candis:
                candis.remove(n)
            if m != '.' and m in candis:
                candis.remove(m)
        for ii in range(i//3 * 3, (i//3 + 1)*3):
            for jj in range(j//3 * 3, (j//3 + 1)*3):
                if self.board[ii][jj] != '.' and self.board[ii][jj] in candis:
                    candis.remove(self.board[ii][jj])
        return candis
    
    
'''
Write a program to solve a Sudoku puzzle by filling the empty cells.
A sudoku solution must satisfy all of the following rules:
Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
Empty cells are indicated by the character '.'.

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.

Solution: Backtracking, DFS
'''
