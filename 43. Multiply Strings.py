class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1, n2 = [], []
        for i in range(len(num1)-1, -1, -1):
            n1.append(ord(num1[i]) - ord('0'))
        for i in range(len(num2)-1, -1, -1):
            n2.append(ord(num2[i]) - ord('0'))
            
        int1, int2 = 0, 0
        t = 1
        for i in n1:
            int1 += i*t
            t *= 10
        t = 1
        
        for i in n2:
            int2 += i*t
            t *= 10
        
        return str(int1*int2)
            
'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.
The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''
            
            
        
            
        
