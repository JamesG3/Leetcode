class Solution:
    """
    :type n: int
    :rtype: int
    Solution: Bit manipulation
    """
    def reverseBits(self, n):
        res = 0
        shift = 31
        
        while shift > -1:
            res += (n & 1) << shift
            shift -= 1
            n >>= 1
            
        return res

# Reverse bits of a given 32 bits unsigned integer.
