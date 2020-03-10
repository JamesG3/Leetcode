class Node():
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.word = None
        
        
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        head = Node()
        for word in words:
            node = head
            for c in word:
                if c not in node.children:
                    node.children[c] = Node()
                node = node.children[c]
            node.is_word = True
            node.word = word
        
        self.board = board
        self.res = set()
        self.height = len(board)
        if not self.height:
            return self.res
        self.width = len(board[0])
        if not self.width:
            return self.res
        
        for i, row in enumerate(board):
            for j, c in enumerate(row):
                node = head
                if c not in node.children:
                    continue
                    
                self.backtracking(i, j, node.children[c])
        return list(self.res)
                   
    # DFS
    def backtracking(self, a, b, node):
        letter = self.board[a][b]
        # use * to prevent loop, each DFS only search one path
        self.board[a][b] = '*'
        
        if node.is_word:
            self.res.add(node.word)
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        
        for x, y in dirs:
            aa, bb = a + x, b + y
            if (0 <= aa < self.height) and \
                (0 <= bb < self.width) and \
                self.board[aa][bb] in node.children:
                
                self.backtracking(aa, bb, node.children[self.board[aa][bb]])
        
        # after traverse this path, reset the original value for next DFS search
        self.board[a][b] = letter
                
'''
Given a 2D board and a list of words from the dictionary, find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Solution: Trie, prefix tree, backtracking, DFS
Time: O(n*m*max_word_length)), where n*m is the size of board, but most of DFS serach may get early terminated
'''
        
        
