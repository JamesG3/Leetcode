class Solution(object):
    def detectCapitalUse(self, word):
        length = len(word)
        l = []
        for w in word:
            l.append(65 <= ord(w) <= 90)
        S = sum(l)
        return S==length or S==0 or (S==1 and l[0]==1)
        
        
                
        
        """
        :type word: str
        :rtype: bool
        """
        
        
        # Given a word, you need to judge whether the usage of capitals in it is right or not.
        # We define the usage of capitals in a word to be right when one of the following cases holds:
        # All letters in this word are capitals, like "USA".
        # All letters in this word are not capitals, like "leetcode".
        # Only the first letter in this word is capital if it has more than one letter, like "Google".
        # Otherwise, we define that this word doesn't use capitals in a right way.
