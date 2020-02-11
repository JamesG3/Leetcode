class Node():
    def __init__(self):
        self.valid = False
        self.child = {}
        self.word = None

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = Node()
        for w in words:
            node = root
            for c in w:
                if c not in node.child:
                    node.child[c] = Node()
                node = node.child[c]
            node.valid = True
            node.word = w
            
        bfs = [root]
        while bfs:
            tmp_bfs = []
            for node in bfs:
                for k,v in node.child.items():
                    if v.valid:
                        tmp_bfs.append(v)
            if not tmp_bfs:
                return sorted([n.word for n in bfs])[0]
            
            bfs = tmp_bfs
            
        return ''

'''
Given a list of strings words representing an English Dictionary, find the longest word in words that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.
If there is no answer, return the empty string.

Solution: Trie, BFS
'''            
                    
                    
            
        
