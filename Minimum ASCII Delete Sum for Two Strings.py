class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        len1, len2 = len(s1) + 1, len(s2) + 1
        dp = [[0] * len2 for i in xrange(len1)]
        
        for i in xrange(len1-2, -1, -1):                    # sum of ASCII value in order to make two strings equal
            dp[i][len2-1] = dp[i+1][len2-1] + ord(s1[i])
        for j in xrange(len2-2, -1, -1):
            dp[len1-1][j] = dp[len1-1][j+1] + ord(s2[j])
        
        # print dp
        # dp[0][0]: make 'sea' and 'eat' equal
        # dp[0][1]: make 'sea' and 'at' equal
        # dp[2][2]: make 'a' and 't' equal
        # ...
        
        for i in xrange(len1-2, -1, -1):
            for j in xrange(len2-2, -1, -1):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] = min(dp[i+1][j] + ord(s1[i]), dp[i][j+1] + ord(s2[j]))   # choose the letter with small ASCII value
                # print dp
                
        return dp[0][0]
        
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        
        # Given two strings s1, s2, find the lowest ASCII sum of deleted characters to make two strings equal.

