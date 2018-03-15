class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        
        dic = {}
        dicsize = 0
        i = 0
        mxlen = 0
        length = len(s)
        
        
        for j in xrange(length):
            if s[j] not in dic:
                dic[s[j]] = 1
                dicsize += 1
            else:
                dic[s[j]] += 1
                
            if dicsize <= k:
                mxlen = max(mxlen, j-i+1)
                
            while dicsize > k:
                dic[s[i]] -= 1
                if dic[s[i]] == 0:
                    del dic[s[i]]
                    dicsize -= 1
                i+=1
        return mxlen
                
        
        
        
        
        
        
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        
        
        # Given a string, find the length of the longest substring T that contains at most k distinct characters.
        # For example, Given s = “eceba” and k = 2,
        # T is "ece" which its length is 3.
