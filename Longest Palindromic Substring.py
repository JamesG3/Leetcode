class Solution(object):
# expand from center
# 2 base cases: s[i]   &&   s[i:i+2]
# O(n^2) time

    def longestPalindrome(self, s):
        length = len(s)
        
        if length == 0:
            return ""
        if length == 1:
            return s
        
        res = s[0]
        maxlen = 1
        
        for i in xrange(length):
            curstr1, curstr2 = "", ""
            maxlen1, maxlen2 = 0, 0
            if i+1 < length and i-1>-1 and s[i+1] == s[i-1]:
                curstr1, maxlen1 = self.expand(i-1, i+1, length, s, s[i])

            if i+1 < length and s[i] == s[i+1]:
                curstr2, maxlen2 = self.expand(i-1, i+2, length, s, s[i:i+2])
            
            maxlen = max(maxlen, maxlen1, maxlen2)
            if maxlen1 == maxlen:
                res = curstr1
            elif maxlen2 == maxlen:
                res = curstr2
                
        return res
            
        
    def expand(self, m, n, length, s, curstr):
        while m>-1 and n<length:
            if s[m] == s[n]:
                curstr = s[m:n+1]
                m-=1
                n+=1
            else:
                break
        return curstr, n-m-1
                    
            
        
        
        
        """
        :type s: str
        :rtype: str
        """
        
        # Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
        
