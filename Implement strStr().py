class Solution(object):
    def strStr(self, haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        return -1
        
        
        
        """
        Implement strStr().
        Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
