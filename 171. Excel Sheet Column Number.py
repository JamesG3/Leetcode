class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        Solution: Convert to math problem, simliar wiht decimal
        Time: O(n)
        Space: O(1)
        """
        res = 0
        length = len(s)
        for i in xrange(length):
            t = length - 1 - i
            res += (26**t) * (ord(s[i]) - 64)
            
        return res

# Given a column title as appear in an Excel sheet, return its corresponding column number.
#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
