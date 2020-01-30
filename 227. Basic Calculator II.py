class Solution:
    def calculate(self, s: str) -> int:
        clean_s = s.replace(' ', '') + '+'
        num = 0
        stack = []
        operator = '+'
        
        for c in clean_s:
            if c.isdigit():
                num = (num * 10) + int(c)
                
            else:
                if operator == '+':
                    stack.append(num)
                elif operator == '-':
                    stack.append(-num)
                elif operator == '*':
                    stack.append(stack.pop() * num)
                elif operator == '/':
                    stack.append(int(stack.pop() / num))
                
                # apply operator in the next round
                num = 0
                operator = c
                
        return sum(stack)
                
'''
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Solution: Stack, Math, trick, String, save operator for next round calculation
Time, Space: O(n)
'''        
                
        
        
