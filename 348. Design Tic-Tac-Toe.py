class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.n = n
        self.board = [[0 for _ in range(n)] for _ in range(n)]
        

    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        self.board[row][col] = player
        win = self.check(row, col)
        return 0 if not win else player
        
        
    def check(self, r, c):
        dirs = [[[0, 1], [0, -1]], [[1, 0], [-1, 0]], [[1, 1], [-1, -1]], [[1, -1], [-1, 1]]]
        base = self.board[r][c]
        cnt = 0
        
        for i in range(self.n):
            if self.board[i][c] != base:
                break
            cnt += 1
        if cnt == self.n:
            return True
        
        cnt = 0
        for i in range(self.n):
            if self.board[r][i] != base:
                break
            cnt += 1
        if cnt == self.n:
            return True
        
        if self.n % 2 != 0 or self.n == 2:
            cnt1, cnt2 = 0, 0
            for i in range(self.n):
                if self.board[i][i] == base:
                    cnt1 += 1
                if self.board[i][self.n-i-1] == base:
                    cnt2 += 1
            
            if cnt1 == self.n or cnt2 == self.n:
                return True
        return False
            
            
        
# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)


'''
Design a Tic-tac-toe game that is played between two players on a n x n grid.

You may assume the following rules:

A move is guaranteed to be valid and is placed on an empty block.
Once a winning condition is reached, no more moves is allowed.
A player who succeeds in placing n of their marks in a horizontal, vertical, or diagonal row wins the game

Solution: Check four directions, traverse and count
Time: O(n)
Space: O(n^2)
'''
