class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        cur_max = prices[-1]
        max_profit = -float('inf')
        
        for i in range(len(prices)-1, -1, -1):
            price = prices[i]
            
            if price <= cur_max:
                profit = cur_max - price
                max_profit = max(max_profit, profit)
                
            if price > cur_max:
                cur_max = price
        return max_profit
    
'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
Example:
    Input: [7,1,5,3,6,4]
    Output: 5


Solution: Greedy
Time: O(n)
Space: O(1)
'''
