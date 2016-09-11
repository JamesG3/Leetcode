from operator import mul

class Solution(object):
    def climbStairs(self, n):
        a=1
        b=n-1
        r=0
        if n%2 == 0:
            while a<b:
                r+=reduce(mul, range(b-a+1,b+1)) / reduce(mul, range(1,a+1))
                a+=1
                b-=1
            return r+2
        elif n%2 == 1:
            while a<b:
                r+=reduce(mul, range(b-a+1,b+1)) / reduce(mul, range(1,a+1))
                a+=1
                b-=1
            return r+1
                
                
                
        """
        :type n: int
        :rtype: int
        use reduce to calculate factorial
        """
        
