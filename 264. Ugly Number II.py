class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        p2, p3, p5 = 0, 0, 0
        
        for i in range(n-1):
            n2 = dp[p2] * 2
            n3 = dp[p3] * 3
            n5 = dp[p5] * 5
            
            min_n = min(n2, n3, n5)
            dp.append(min_n)
            
            if n2 == min_n:
                p2 += 1
            if n3 == min_n:
                p3 += 1
            if n5 == min_n:
                p5 += 1

        return dp[-1]
            
'''
Write a program to find the n-th ugly number.
Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. 

Solution: DP, pointers, use three pointers, update dp with the smallest one
Time, Space: O(n)
'''    
        
