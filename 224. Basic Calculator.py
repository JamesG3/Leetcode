class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        operand = 0
        res = 0
        sign = 1
        
        for c in s:
            if c.isdigit():
                operand = (operand * 10) + int(c)
                
            elif c == '+':
                res += sign * operand
                # reset after calculation
                sign = 1
                operand = 0
                
            elif c == '-':
                # add prev result
                res += sign * operand
                sign = -1
                operand = 0
                
            # push global res to stack, reset res for local usage
            elif c == '(':
                stack.append(res)
                stack.append(sign)
                
                sign = 1
                res = 0
                
            elif c == ')':
                res += sign * operand
                # pop sign
                res *= stack.pop()
                # pop prev res
                res += stack.pop()
                
                operand = 0
                
        # add the last part
        return res + sign * operand
    
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Solution: Stack, math, operand & sign update
Time, Space: O(n)
'''

