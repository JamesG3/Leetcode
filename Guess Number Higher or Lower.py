# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        if guess(1)==0:
            return 1
        elif guess(n)==0:
            return n
        r=n/2
        low=1
        high=n
        while guess(r)!=0 :
            if guess(r)==1:
                low=r
                r+=(high-low)/2
                
            elif guess(r)==-1:
                high=r
                r-=(high-low)/2
        return r
                
        """
        :type n: int
        :rtype: int
        """
