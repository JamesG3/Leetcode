class Solution(object):
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        Solution: Recursive
        """
        
        if N < 1:
            return 0
        if N == 1:
            return 1
        
        return self.fib(N - 1) + self.fib(N - 2)
            
            
# The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. 
# Given N, calculate F(N).
