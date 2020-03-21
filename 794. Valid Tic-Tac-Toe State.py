class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        self.board = board
        player1, player2 = 'X', 'O'
        cnt1, cnt2 = 0, 0
        for row in board:
            for c in row:
                if c == player1:
                    cnt1 += 1
                elif c == player2:
                    cnt2 += 1
        
        if not (cnt1 == cnt2 or cnt1 - 1 == cnt2):
            return False
        
        win1 = self.checkwin(player1)
        win2 = self.checkwin(player2)
        if win1 and not cnt1 > cnt2:
            return False
        if win2 and not cnt1 == cnt2:
            return False
        
        return True
    
    def checkwin(self, player):
        for i in range(3):
            if len([self.board[i][j] for j in range(3) if self.board[i][j] == player]) == 3:
                return True
            if len([self.board[j][i] for j in range(3) if self.board[j][i] == player]) == 3:
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] == player or \
            self.board[2][0] == self.board[1][1] == self.board[0][2] == player:
            return True
        
        return False
'''
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.

The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.

Here are the rules of Tic-Tac-Toe:

Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

Solution: Edge case, rule, simulation
Time: O(1), because the board is a costant space

''' 
