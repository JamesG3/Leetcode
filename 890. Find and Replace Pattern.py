class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        Solution: Convert to a standard pattern, then compare
        Time: O(n)
        Space: O(n)
        """
        pattern = self.convert(pattern)
        res = []
        for w in words:
            cur_pattern = self.convert(w)
            if cur_pattern == pattern:
                res.append(w)
                
        return res
        
        
    def convert(self, word):
        mapping = {}
        pattern = []
        p = 0
        for i, c in enumerate(word):
            if c not in mapping:
                mapping[c] = p
                p += 1
                pattern.append([i])
                
            else:
                pattern[mapping[c]].append(i)
                
        return pattern
                
        
# You have a list of words and a pattern, and you want to know which words in words matches the pattern.

# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.

# (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)

# Return a list of the words in words that match the given pattern. 

# You may return the answer in any order.
