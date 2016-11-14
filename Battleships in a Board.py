class Solution(object):
    def countBattleships(self, board):
        ans=0
        for n in range(0,len(board)):
            for m in range(0,len(board[0])):
                if board[n][m] == "X":
                    markheadV=0           #initialize the vertical mark
                    if n==0 or (n>0 and board[n-1][m] == "."):
                        markheadV=1       #if this X is a vertical head of a ship
                    markheadH=0
                    if m==0 or (m>0 and board[n][m-1] == "."):
                        markheadH=1       #if this X is also a horizontal head of a ship
                    if markheadH==1 and markheadV==1:   #if this X is a head, ans+=1.
                        ans+=1
                    #discard the other part of a ship, add ans only if head
        return ans
        
        """
        
        Given an 2D board, count how many different battleships are in it. The battleships are represented with 'X's, empty slots are represented with '.'s. You may assume the following rules:

        - You receive a valid board, made of only battleships or empty slots.
        - Battleships can only be placed horizontally or vertically. In other words, they can only be made of the shape 1xN (1 row, N columns) or Nx1 (N rows, 1 column), where N can be of any size.
        - At least one horizontal or vertical cell separates between two battleships - there are no adjacent battleships.
        
        :type board: List[List[str]]
        :rtype: int
        """
