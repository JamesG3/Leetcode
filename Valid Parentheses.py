class Solution(object):
    def isValid(self, s):
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False
                    
                elif c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                    
                elif c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                else:
                    stack.append(c)
        
        return len(stack) == 0



#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.
