class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num
        
        while l <= r:
            m = (l + r) // 2
            sqrt = m**2
            if sqrt == num:
                return True
            
            elif sqrt > num:
                r = m - 1
            else:
                l = m + 1
        return False

'''
Given a positive integer num, write a function which returns True if num is a perfect square else False.
Note: Do not use any built-in library function such as sqrt.    

Solution: Binary Search
Time: O(log(n))
Space: O(1)
'''
