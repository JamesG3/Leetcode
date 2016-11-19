class Solution(object):
    def isIsomorphic(self, s, t):
        dics={}
        dict={}
        spattern=[]
        tpattern=[]
        i=1
        
        for n in s:
            if n not in dics:           #using i represents the pattern of letters
                dics[n]=i
                i+=1
            spattern.append(dics[n])    #showing the pattern of s
        
        i=1                             #reset i
        for m in t:
            if m not in dict:
                dict[m]=i
                i+=1
            tpattern.append(dict[m])    #showing the pattern of s
            
        return tpattern==spattern
                
        
        """
        Given two strings s and t, determine if they are isomorphic.
        For example,
        Given "egg", "add", return true.
        Given "foo", "bar", return false.
        
        :type s: str
        :type t: str
        :rtype: bool
        """
        
