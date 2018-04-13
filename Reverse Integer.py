class Solution:
    def reverse(self, x):
        s = cmp(x, 0)
        res = 0
        
        x = s*x
        while x > 0:
            res = res*10 + x%10
            x /= 10
            
        res = s*res
        return res if -2**31 <= res <= 2**31-1 else 0
        """
        :type x: int
        :rtype: int
        """
        
        
        
        # Given a 32-bit signed integer, reverse digits of an integer.

