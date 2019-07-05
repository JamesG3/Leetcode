class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        Solution: Using Hash table (dic and set)
        Time: O(n)
        Space: O(n)
        """
        dic = {}
        found = set()
        
        for i,c1 in enumerate(s):
            c2 = t[i]
            if c1 in dic:
                if dic[c1] != c2:
                    return False
            else:
                if c2 in found:
                    return False
                else:
                    dic[c1] = c2
                    found.add(c2)
                    
        return True
                    
# Given two strings s and t, determine if they are isomorphic.
# Two strings are isomorphic if the characters in s can be replaced to get t.
# All occurrences of a character must be replaced with another character while preserving the order of characters.
# No two characters may map to the same character but a character may map to itself.
