class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=0
        while(n>=5):
            count+=n/5
            n=n/5
        return count

        
#Given an integer n, return the number of trailing zeroes in n!.
