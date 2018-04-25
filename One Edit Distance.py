class Solution(object):
    
    # two pointers solution, AC
    def isOneEditDistance(self, s, t):
        slen = len(s)
        tlen = len(t)
        
        if abs(slen - tlen) > 1:
            return False
        
        l = min(slen, tlen)
        i, j = 0, 1
        
        while i < l and s[i] == t[i]:
            i+=1
        while j < (l-i+1) and s[-j] == t[-j]:
            j += 1
            
        return max(slen, tlen) == i + j
       
       
      
    # dp solution, TLE
    def isOneEditDistance(self, s, t):
        slen = len(s)
        tlen = len(t)
        
        if not slen or not tlen:
            return max(slen, tlen) == 1
        
        dist = [[0 for _ in xrange(tlen+1)] for _ in xrange(slen+1)]
        
        for i in xrange(slen+1):
            dist[i][0] = i
            
        for j in xrange(tlen+1):
            dist[0][j] = j
            
        for i in xrange(1, slen+1):
            for j in xrange(1, tlen+1):
                if s[i-1] == t[j-1]:
                    dist[i][j] = dist[i-1][j-1]
                else:
                    dist[i][j] = min(dist[i-1][j], dist[i][j-1], dist[i-1][j-1]) + 1
                    
        return dist[-1][-1] == 1
            
        
        
        
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        
        # Given two strings s and t, determine if they are both one edit distance apart.
        # Note: 
        # There are 3 possiblities to satisify one edit distance apart:
        # Insert a character into s to get t
        # Delete a character from s to get t
        # Replace a character of s to get t
        
