class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 1:
            return True
        if n == 4:
            return False
        
        cur_sum = 0
        while n:
            cur_sum += (n%10) ** 2
            n /= 10
            
        return self.isHappy(cur_sum)

"""
Write an algorithm to determine if a number is "happy".
Example: 19 is a happy number
1**2 + 9**2 = 82
8**2 + 2**2 = 68
6**2 + 8**2 = 100
1**2 + 0**2 + 0**2 = 1
"""

# Solution Explaination: Numbers that are happy follow a sequence that ends in 1. All unhappy numbers follow sequences that eventually reach the eight-number cycle
# 4 → 16 → 37 → 58 → 89 → 145 → 42 → 20 → 4 → ...


