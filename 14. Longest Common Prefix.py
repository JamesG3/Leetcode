class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        Solution: Horizontal Scanning, use the new prefix to find common prefix on next string
        Time: O(n)
        Space: O(1)
        """
        length = len(strs)
        if length == 0:
            return ""
        if length == 1:
            return strs[0]
        
        prefix = self.commonPrefix(strs[0], strs[1])
        for i in xrange(1, length):
            prefix = self.commonPrefix(prefix, strs[i])
            
        return prefix
            
        
    def commonPrefix(self, str1, str2):
        prefix = ""
        len1, len2 = len(str1), len(str2)
        for i in xrange(min([len1, len2])):
            if str1[i] == str2[i]:
                prefix += str1[i]
                
        return prefix

    
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
