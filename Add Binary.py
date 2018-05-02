class Solution(object):
    # bit solution
    def addBinary(self, a, b):
        carry = 0
        alen = len(a)
        blen = len(b)
        res = ""
        
        if alen < blen:
            a = "0" * (blen-alen) + a
            alen = blen
        elif blen < alen:
            b = "0" * (alen-blen) + b
            blen = alen
            
        for j in xrange(alen):
            res = str((int(a[~j]) + int(b[~j]) + carry) % 2) + res
            carry = int((int(a[~j]) + int(b[~j]) + carry) / 2)
            
        if carry:
            res = "1" + res
            
        return res
        
    
    
    
    # bin solution
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
        
