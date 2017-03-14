class Solution(object):
    def integerBreak(self, n):
        # when n is less or equal than 3
        if n == 3:
            return 2
        elif n == 2 or n == 1:
            return 1

        # when n is larger than 3, at least can be break into one 3 and another number
        # try to break as many 3 as possible (unless the left number is 1)
        
        if n % 3 == 0:
            return 3**(n/3)
        elif n % 3 == 1:
            return 3**((n/3)-1)*4
        elif n % 3 > 1:
            return 3**(n/3) * (n%3)
        """
        :type n: int
        :rtype: int
        """
        
        
        #Given a positive integer n, break it into the sum of at least two positive integers and maximize the product of those integers. 
        #Return the maximum product you can get.
        #For example, given n = 2, return 1 (2 = 1 + 1); given n = 10, return 36 (10 = 3 + 3 + 4).
