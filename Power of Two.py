class Solution(object):
    # math solution (mod) O(1)
    def isPowerOfTwo(self, n):
        if n <= 0:
            return False

        return not (2**31 % n)
    
    
    
    
    
    # string solution, O(n)
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if(n<=0):
            return False
        else:
            return bin(n).count('1')==1
        
        
#        if(n==0):
#            return False
#        while(n!=1):
#            if(n%2==0):
#                n/=2
#            else:
#                return False
#        return True
        
#Given an integer, write a function to determine if it is a power of two. 
