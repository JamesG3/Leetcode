class Solution(object):

    # DP solution
    def minDistance(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        
        if len1 == 0 or len2 == 0:
            return max(len1, len2)
        
        dist = [[0 for _ in xrange(len2+1)] for _ in xrange(len1+1)]
        
        for i in xrange(len1+1):
            dist[i][0] = i
        for j in xrange(len2+1):
            dist[0][j] = j
            
        for i in xrange(1, len1+1):
            for j in xrange(1, len2+1):
                if word1[i-1] == word2[j-1]:
                    dist[i][j] = dist[i-1][j-1]
                else:
                    dist[i][j] = min(dist[i-1][j], dist[i][j-1], dist[i-1][j-1]) + 1
                    
        return dist[-1][-1]
        

        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        
        
        # http://www.dreamxu.com/books/dsa/dp/edit-distance.html
        # Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

        # You have the following 3 operations permitted on a word:
        # Insert a character
        # Delete a character
        # Replace a character
