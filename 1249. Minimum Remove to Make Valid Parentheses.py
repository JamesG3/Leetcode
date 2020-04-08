class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        keep = [True for c in s]
        stack = []
        
        for i, c in enumerate(s):
            if c == '(':
                stack.append([c, i])
            elif c == ')':
                while stack and stack[-1][0] == ')':
                    invalid_c, invalid_i = stack.pop()
                    keep[invalid_i] = False
                
                if stack and stack[-1][0] == '(':
                    stack.pop()
                else:
                    stack.append([c, i])
        
        for invalid_c, invalid_i in stack:
            keep[invalid_i] = False
                
        return ''.join([_ for i, _ in enumerate(s) if keep[i]])
        
'''
Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Solution: Stack, two pass,
    the first pass using stack to get all Parentheses which need to be removed
    the second pass generate the output valid string
    
Time, Space: O(n)
'''
