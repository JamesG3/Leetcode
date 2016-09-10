class Solution(object):
    def firstUniqChar(self, s):
        d={}
        for n in s:
            if n in d:
                d[n]+=1
            else:
                d[n]=1
        for x in s:
            if d[x]==1:
                return s.find(x)
        return -1
                
                
        """
        :type s: str
        :rtype: int
        """
