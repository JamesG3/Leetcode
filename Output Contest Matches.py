class Solution(object):
    def findContestMatch(self, n):
        teamList = map(str, xrange(1, n+1))
        while n != 1:
            for i in xrange(n>>1):
                teamList[i] = "(" + teamList[i] + "," + teamList[n-i-1] + ")"
            n = n>>1
        return teamList[0]
        
        
        """
        :type n: int
        :rtype: str
        """
        
