class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        # two pointers solution
        res = ""
        j = length = len(s)
        
        for i in xrange(length-1, -1, -1):
            if s[i] == " ":
                j = i
            elif i == 0 or s[i-1] == " ":
                if res:
                    res += " "
                res += s[i:j]
        return res
                
           
                
        # one line solution
        return " ".join(s.split()[::-1])
