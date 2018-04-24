class Solution(object):

    # bit-manipulation, binary search
    def divide(self, dividend, divisor):
        res = 0
        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        
        
        while divisor <= dividend:
            i, tmp = 1, divisor
            while tmp <= dividend:
                dividend -= tmp
                res += i
                
                tmp <<= 1
                i <<= 1
                
        res *= sign
        
        return min(max(-2**31, res), 2**31-1)
                
  
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        
        
        
        # Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
        # Return the quotient after dividing dividend by divisor.\
        # The integer division should truncate toward zero.
        
        
        # Both dividend and divisor will be 32-bit signed integers.
        # The divisor will never be 0.
        # Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. 
        # For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
