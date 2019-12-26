class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for n in num:
            while k and stack and n < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(n)
        
        stack = stack[:-k] if k else stack
        res = ''.join(stack).lstrip('0')
        return res if res else '0'
            
'''
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

Note:

The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Solution: Stack, Greedy
Time, Space = O(n)
'''
