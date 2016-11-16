class Solution(object):
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        counter=0
        while len(s)!=0 and len(g)!=0:
            if s[0]<g[0]:
                del s[0]
            else:
                del s[0]
                del g[0]
                counter+=1
        return counter
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
