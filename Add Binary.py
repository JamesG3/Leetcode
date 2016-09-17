class Solution(object):
    def addBinary(self, a, b):
        c=int(a,2)+int(b,2)
        c=bin(int(str(c),10))[2:]
        return c
        """
        :type a: str
        :type b: str
        :rtype: str
        Given two binary strings, return their sum (also a binary string).
        """
        
