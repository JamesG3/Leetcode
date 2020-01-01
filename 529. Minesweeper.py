from copy import deepcopy
class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.height = len(board)
        self.width = len(board[0])
        self.board = board
        
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        
        if board[x][y] == 'E':
            stack = [[x, y]]
            visted = set()
            
            while stack:
                i, j = stack.pop()
                if (i,j) in visted:
                    continue
                    
                has_mine, blanks = self.check_neighbor(i, j)
                # if there is any mine next to this point, update it to the number of mines
                if has_mine:
                    board[i][j] = str(has_mine)
                    continue
                
                # update the content from 'E' to 'B'
                board[i][j] = 'B'
                visted.add((i, j))
                stack += blanks
                
        return board
                    
            
        
    def check_neighbor(self, x, y):
        blanks = []
        has_mine = 0
        dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [1, -1], [1, 1], [-1, 1], [-1, -1]]
        
        for i, j in dirs:
            m, n = x+i, y+j
            if not(0 <= m < self.height and 0 <= n < self.width):
                continue
                
            if self.board[m][n] == 'M':
                has_mine += 1
            
            elif self.board[m][n] == 'E':
                blanks.append([m, n])
        # return how many mines surround [x, y], and all blank squares
        return has_mine, blanks
                
            
'''
Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board. 'M' represents an unrevealed mine, 'E' represents an unrevealed empty square, 'B' represents a revealed blank square that has no adjacent (above, below, left, right, and all 4 diagonals) mines, digit ('1' to '8') represents how many mines are adjacent to this revealed square, and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the unrevealed squares ('M' or 'E'), return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed, then change it to revealed blank ('B') and all of its adjacent unrevealed squares should be revealed recursively.
If an empty square ('E') with at least one adjacent mine is revealed, then change it to a digit ('1' to '8') representing the number of adjacent mines.
Return the board when no more squares will be revealed.

Solution: DFS, Hashset, Stack, State Machine
Time, Space: O(n)
'''  
        
