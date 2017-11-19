class Solution(object):
    def countSubstrings(self, s):
        count = 0
        Length = len(s)
        
        for i in xrange(2*Length-1):
            left = i/2                      # update center string, could be one char or two char
            right = i/2 + i%2
            
            while left >= 0 and right < Length and s[left] == s[right]:     # check palindromic string from each center
                left -= 1
                right += 1
                count += 1
        return count
        
        """
        :type s: str
        :rtype: int
        """
        # Given a string, your task is to count how many palindromic substrings in this string.
        # The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.
