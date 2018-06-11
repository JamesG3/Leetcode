class Solution(object):
    
    # Newton's method
    def mySqrt(self, x):
        r = x
        
        while r**2 > x:
            r = (r + x/r) / 2
        return r
            
        
        """
        :type x: int
        :rtype: int
        """
        
        # Implement int sqrt(int x).
        # Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
        # Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.
