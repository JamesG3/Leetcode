class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.split(" ")
        for i in xrange(len(s)):
            if len(s[~i]) != 0:
                return len(s[~i])
            
        return 0
        """
        :type s: str
        :rtype: int
        """
        
        
        # Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
        # If the last word does not exist, return 0.
        # Note: A word is defined as a character sequence consists of non-space characters only.
        
