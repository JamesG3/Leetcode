class Solution(object):
    def findTheDifference(self, s, t):
        d={}
        for n in s:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        for x in t:
            if x not in d or t.count(x)!=d[x]:
                return x

                
        """
        :type s: str
        :type t: str
        :rtype: str
        """
