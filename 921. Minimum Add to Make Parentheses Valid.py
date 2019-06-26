class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        Solution: Stack
        Time: O(n)
        Space: O(n)
        """
        stack = []
        
        for s in S:
            if s == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                    continue
            stack.append(s)
        return len(stack)
            
        
# Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
