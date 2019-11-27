from copy import deepcopy

class Solution(object):    
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
        self.board = board
        self.word = word
        self.word_len = len(word)
        self.length = len(board[0])
        self.height = len(board)
        
        for i,w in enumerate(board):
            for j,c in enumerate(w):
                if self.find(i, j, 0):
                    return True    
        return False
        
                   
    def find(self, i, j, word_i):
        if (not 0 <= i < self.height) or (not 0 <= j < self.length) or (self.board[i][j] != self.word[word_i]):
            return False
        
        if word_i == self.word_len - 1:
            return True
        
        # use empty str to prevent loop, don't need to store visted nodes
        char = ''
        char, self.board[i][j] = self.board[i][j], char
        
        for dir_i, dir_j in self.directions:
            if self.find(i+dir_i, j+dir_j, word_i+1):
                return True
        
        self.board[i][j] = char
        return False
    
'''
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, 
where "adjacent" cells are those horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Solution: graph DFS
Time: O(4nm)
Space: extra O(1)
'''
