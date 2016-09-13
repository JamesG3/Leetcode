class Solution(object):
    def lengthOfLastWord(self, s):
        s=list(s)
        s.reverse()
        count=0
        if s==[]:
            return 0
        else:
            for item in s:
                if item != " ":
                    count+=1
                elif count!=0:
                    break
        return count
            
        """
        :type s: str
        :rtype: int
        Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
        If the last word does not exist, return 0.
        Note: A word is defined as a character sequence consists of non-space characters only.
        For example, 
        Given s = "Hello World",
        return 5.
        """
        
