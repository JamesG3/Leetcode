class Solution(object):
    def isValidSudoku(self, board):
        
        for i in xrange(9):
            set1 = set()
            for j in xrange(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num not in set1:
                    set1.add(num)
                else:
                    return False
                
        for j in xrange(9):
            set1 = set()
            for i in xrange(9):
                num = board[i][j]
                if num == '.':
                    continue
                if num not in set1:
                    set1.add(num)
                else:
                    return False
                
        for i in xrange(3):
            for j in xrange(3):
                set1 = set()
                for k in xrange(9):
                    m, n = k/3 + i*3, k%3 + j*3
                    num = board[m][n]
                    if num == '.':
                        continue    
                    if num not in set1:
                        set1.add(board[m][n])
                        
                    else:
                        return False
                    
        return True
                    
                   
        
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        
        # Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

        # Each row must contain the digits 1-9 without repetition.
        # Each column must contain the digits 1-9 without repetition.
        # Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
        
        # The Sudoku board could be partially filled, where empty cells are filled with the character '.'.


        
