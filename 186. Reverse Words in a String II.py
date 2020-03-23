class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = s[::-1]
        l, r = 0, 0
        while r < len(s):
            if s[r] == ' ':
                s[l:r] = s[l:r][::-1]
                l = r + 1
            r += 1
        s[l:r] = s[l:r][::-1]
        return
                
'''
Given an input string , reverse the string word by word. 
Note: 
A word is defined as a sequence of non-space characters.
The input string does not contain leading or trailing spaces.
The words are always separated by a single space.
Follow up: Could you do it in-place without allocating extra space?

Solution: Python list slice, in place
Time: O(n)
Space: O(1)
'''


