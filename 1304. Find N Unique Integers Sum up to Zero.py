class Solution:
    def sumZero(self, n: int) -> List[int]:
        res = [_ for _ in range(1, n//2+1)]
        res += [-_ for _ in res]
        
        if n % 2 == 0:
            return res
        else:
            return res + [0]
            
            
'''
Given an integer n, return any array containing n unique integers such that they add up to 0.
Solution: 
    Return an array where the values are symmetric. (+x , -x).
    If n is odd, append value 0 in your returned array.
Time: O(n)
Space: O(n)
'''
