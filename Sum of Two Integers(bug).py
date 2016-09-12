class Solution(object):
    def getSum(self,a,b):
        t=0
        while (b!=0):
            t=a&b
            a=a^b
            b=t<<1
        return a
        """
        :type a: int
        :type b: int
        :rtype: int
        Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.
        """
        
