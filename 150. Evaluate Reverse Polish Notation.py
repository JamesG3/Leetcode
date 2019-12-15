class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            '*': lambda x,y: x*y,
            '/': lambda x,y: x/y,
            '-': lambda x,y: x-y,
            '+': lambda x,y: x+y
        }
        
        stack = []
        
        for item in tokens:
            if item not in operations:
                stack.append(int(item))
            else:
                x2 = stack.pop()
                x1 = stack.pop()
                res = int(operations[item](x1, x2))
                stack.append(res)
                
        return stack[-1]

'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.


RPN - stack based expression - put operators after elements
Solution: stack
Time & Space: O(n)
'''
