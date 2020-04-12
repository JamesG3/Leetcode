class Node():
    def __init__(self):
        self.nxt = {}
        self.word = ''

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.head = Node()
        self.res = []
        for word in wordDict:
            node = self.head
            for c in word:
                if c not in node.nxt:
                    node.nxt[c] = Node()
                node = node.nxt[c]
            node.word = word
        
        self.backtrack([], s)
        return self.res
                    

    def backtrack(self, cur_res, remain):
        if not remain:
            self.res.append(' '.join(cur_res))
            
        words = []
        
        node = self.head
        cur_i = 0
        for c in remain:
            if c in node.nxt:
                cur_i += 1
                node = node.nxt[c]
                if node.word:
                    words.append([node.word, cur_i])
            else:
                break
        
        for w, i in words:
            self.backtrack(cur_res + [w], remain[i:])
            
'''
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Solution: Trie Tree, backtracking
'''
