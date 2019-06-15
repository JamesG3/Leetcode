class Solution(object):
    """
    :type s: str
    :rtype: bool
    """
    def isValid(self, s):
        dic = {')':'(', ']': '[', '}': '{'}
        stack = []
        
        for c in s:
            if c in ('(', '[', '{'):
                stack.append(c)
            else:
                if stack and stack[-1] == dic[c]:
                    stack.pop()
                else:
                    return False
                
        return stack == []



#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
