class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # DP solution, actually same as climb stairs, accumulate the possiblities from previous step(s)
        dp = [0 for _ in range(amount + 1)]
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        return dp[-1]
    
    
    
'''
You are given coins of different denominations and a total amount of money. Write a function to compute the number of combinations that make up that amount. You may assume that you have infinite number of each kind of coin.

Solution: DP, actually same as climb stairs, accumulate the possiblities from previous step(s)
Time: O(n * len(coins))
Space: O(n)
'''
