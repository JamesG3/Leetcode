class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 1:
            return True
        if num <= 0:
            return False
        
        for n in [2, 3, 5]:
            if num%n:
                continue
            while num % n == 0:
                num //= n
        return num == 1
            
        
'''
Write a program to check whether a given number is an ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

Solution: Math
'''
