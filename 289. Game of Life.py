class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changed = set()
        dirs = [[0, 1], [1, 0], [1, 1], [0, -1], [-1, 0], [-1, -1], [1, -1], [-1, 1]]
        height = len(board)
        width = len(board[0]) if height != 0 else 0
        
        if not (width and height):
            return board
        
        for i, row in enumerate(board):
            for j, n in enumerate(row):
                live_nei = 0
                for x, y in dirs:
                    ii, jj = x + i, y + j
                    if (0 <= ii < height) and (0 <= jj < width):
                        if (ii, jj) not in changed:
                            live_nei += board[ii][jj]
                        else:
                            live_nei += 0 if board[ii][jj] else 1
                
                if board[i][j]:
                    if live_nei < 2 or live_nei > 3:
                        board[i][j] = 0
                        changed.add((i, j))
                else:
                    if live_nei == 3:
                        board[i][j] = 1
                        changed.add((i, j))
        return board
                    
        
'''
Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Return the next status base on the given board

Solution: Hashset, Traverse and mark, in-place
Time: O(nm)
Space: O(nm)
'''
