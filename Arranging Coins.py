class Solution(object):
    def arrangeCoins(self, n):
        return int(math.sqrt(2*n+0.25)-0.5)
        
        
        """
        :type n: int
        :rtype: int
        
        You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
        Given n, find the total number of full staircase rows that can be formed.
        n is a non-negative integer and fits within the range of a 32-bit signed integer.
        
        
        (1+h)*h/2 = n.max
        h+h**2 = 2*n.max
        h+h**2+1/4 = 2*n.max+1/4
        (h+1/2)**2 = 2*n.max+1/4
        h+1/2 = sqrt(2*n.max+1/4)
        h = sqrt(2*n.max+1/4)-1/2
        
        """
