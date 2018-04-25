class Solution(object):
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        
        
        dp = [[0 for _ in xrange(len2+1)] for _ in xrange(len1+1)]
        
        for i in xrange(1, len1+1):
            for j in xrange(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i][j-1], dp[i-1][j])
                    
        return len1 + len2 - dp[-1][-1]
                    
        
        
        
        
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        # Given two words word1 and word2, find the minimum number of steps required to make word1 and word2 the same, 
        # where in each step you can delete one character in either string.

