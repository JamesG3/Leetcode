class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        Solution: Only check the head of ship
        Time: O(mn)
        Space: O(1)
        """
        counter = 0
        length, height = len(board[0]), len(board)
        for i in xrange(length):
            for j in xrange(height):
                if board[j][i] == 'X':
                    if (j == 0 or board[j-1][i] == '.') and (i == 0 or board[j][i-1] == '.'):
                        counter += 1    
        return counter
        
"""
Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

- You receive a valid board, made of only battleships or empty slots.
- Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
- At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.

:type board: List[List[str]]
:rtype: int
"""
