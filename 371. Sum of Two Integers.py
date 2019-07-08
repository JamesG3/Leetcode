import ctypes

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        Solution: Bitwise operation, using ctypes to force float32
        """
        if b == 0:
            return a
        
        else:
            carry = ctypes.c_int32(a&b)
            return self.getSum(a^b, carry.value<<1)
        
# Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
