class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        length = len(prices)
        if length < 2:
            return 0
        
        current = 0
        prev = 0
        profit = -prices[0]
        
        for i in xrange(1, length):
            current, prev, profit = prices[i]+profit, max(prev, current), max(profit, prev-prices[i])
            
        return max(prev, current)
        
        # current is the profit if the stock is sold in current day
        # prev is a parameter to always save the larger "current" in the previous state machine
        # profit is a parameter save the accumulation money.
        
