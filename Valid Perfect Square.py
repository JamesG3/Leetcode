class Solution(object):
    def isPerfectSquare(self, num):
        if num<=0:
            return False
        i=1;
        while i<=num/i:                     #Find sqrt(num) by calculating i**2
            if i * i == num:
                return True
            else:
                i+=1;
        return False                        #If i > sqrt(num), then give up finding next i and return False
        """
        :type num: int
        :rtype: bool
        
        Given a positive integer num, write a function which returns True if num is a perfect square else False.
        Do not use any built-in library function such as sqrt.
        """
        
