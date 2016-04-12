class Solution(object):
    ans =[0]
    def numSquares(self, n):
        if len(self.ans)<= n:
            perfectSqr= []
            for v in xrange(1, int(math.sqrt(n))+ 1):
                perfectSqr.append(v**2)
            for i in xrange(len(self.ans), n+1):
                self.ans.append(min(1 + self.ans[i-sqr] for sqr in perfectSqr if sqr <= i))
        return self.ans[n]  
        """
        :type n: int
        :rtype: int
        """
        
        # Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

        # For example, given n = 12, return 3 because 12 = 4 + 4 + 4; given n = 13, return 2 because 13 = 4 + 9. 
