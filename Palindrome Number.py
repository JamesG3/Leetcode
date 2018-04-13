class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        
        num = 0
        tmp = x
        while tmp > 0:
            num = num*10 + tmp%10
            tmp /= 10
            
        return num == x
        
        
        """
        :type x: int
        :rtype: bool
        """
        
        # Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
        # Coud you solve it without converting the integer to a string?

