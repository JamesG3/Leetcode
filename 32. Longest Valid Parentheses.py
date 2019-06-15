class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        Stack solution
        """
        cur_max = 0
        
        # initialize the bottom of stack
        stack = [-1]
        
        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                if stack:
                    cur_max = max(cur_max, i-stack[-1])
                
                # if the stack is empty, reset the stack bottom using curent ')' index
                else:
                    stack.append(i)
                
        return cur_max
