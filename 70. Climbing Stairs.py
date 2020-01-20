class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [1, 2]
        if n < 2:
            return 1
        
        for i in range(3, n+1):
            dp.append(dp[-1] + dp[-2])
            
        return dp[-1]
            
'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Solution: DP, all count for previous 1step + previous 2steps = count for current step
'''
