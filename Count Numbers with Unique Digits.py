class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        ans = []                            # record the amount of numbers for each range
        for i in xrange(1, n+1):
            ans.append(self.helper(i))
        return sum(ans)+1                   # sum up every range and, add 1 (for 0)
            
        
    def helper(self, n):            # calculate the amount of numbers for each range (0-9, 10-99, 100-999 ....)
        if n == 1:
            return 9
        elif n > 1:
            ans = 9
            while n != 1:
                ans *= (9-n+2)
                n -= 1
            return ans
        
        """
        :type n: int
        :rtype: int
        """
        
        
        #Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.
        #Given n = 2, return 91. (The answer should be the total numbers in the range of 0 ≤ x < 100, excluding [11,22,33,44,55,66,77,88,99])
