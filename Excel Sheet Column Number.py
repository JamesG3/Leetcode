class Solution(object):
    def titleToNumber(self, s):
        length = len(s)
        
        base = 0
        for i in xrange(1, length):     #calculate the index of "Z**Z" with length (len(s)-1)
            base += 26 ** i             #if s is sigle digit, then jump to next step, base is still 0
        
        digit = length
        base += 1                       #from "Z*Z" to A**A needs 1 more index
        
        for n in s:
            base += (ord(n)-ord('A')) * 26**(digit-1)   #calculate "******" - "ZZZZZZ" and add to the current base
            digit -= 1
            
        return base
        
        """
        :type s: str
        :rtype: int
        """
        
        #Given a column title as appear in an Excel sheet, return its corresponding column number.
        #For example:
        # A -> 1
        # Z -> 26
        # AA -> 27
        # ZZ -> 702
