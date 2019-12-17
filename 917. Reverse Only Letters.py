class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        stack = [c for c in S if c.isalpha()]
        res = []
        for c in S:
            if c.isalpha():
                res.append(stack.pop())
            else:
                res.append(c)
        return ''.join(res)
    
    
'''
Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.

Solution: Stack
Time & Space: O(n)
'''
