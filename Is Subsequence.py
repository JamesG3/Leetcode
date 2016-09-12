class Solution(object):
    def isSubsequence(self, s, t):
        s1=list(s)
        for n in s1:
            if n not in t:
                return False
            else:
                t=t[t.find(n)+1:]
        return True
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
