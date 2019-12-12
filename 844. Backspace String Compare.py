class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        return self.helper(S) == self.helper(T)
        
    def helper(self, s):
        stack = []
        for c in s:
            if c == '#':
                if stack:
                    stack.pop()
                    
            else:
                stack.append(c)
        return ''.join(stack)
    
'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

Solution: Stack
Time & Space: O(m+n)
'''
