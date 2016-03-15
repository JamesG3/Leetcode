class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return sorted(s)==sorted(t)        #brief version
        
        
#        S=[]
#        T=[]
#        for n in s:
#            S.append(n)
#        for m in t:
#            T.append(m)
        
#        S.sort()
#        T.sort()
#        if(S==T):
#            return True
#        else:
#            return False
