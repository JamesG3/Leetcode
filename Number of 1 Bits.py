class Solution(object):
    def hammingWeight(self, n):
        return bin(n).count('1')
        """
        :type n: int
        :rtype: int
        """
        #Write a function that takes an unsigned integer and returns the number of ’1' bits it has (also known as the Hamming weight).
