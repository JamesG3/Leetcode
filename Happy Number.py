class Solution(object):
    def isHappy(self, n):
        
        while n != 42:                #42 is a conclusion after experiment
            sum=0
            for m in map(int,str(n)):
                sum += m**2
            n=sum
            
            if n == 1:
                return True
                
        return False
        """
        :type n: int
        :rtype: bool

        Write an algorithm to determine if a number is "happy".
        Example: 19 is a happy number
        1**2 + 9**2 = 82
        8**2 + 2**2 = 68
        6**2 + 8**2 = 100
        1**2 + 0**2 + 0**2 = 1
        """
        
