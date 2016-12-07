class Solution(object):
    def maxProfit(self, prices):
        if len(prices)<2:
            return 0
            
        currentmax=prices[-1]
        currentmin=prices[-1]
        profit=0
    
        for i in range(len(prices)-2, -1, -1):          #from latest price to eariler price
            if prices[i]<currentmin:                #always save the minimum price
                currentmin=prices[i]
            if prices[i]>currentmin:                #enter another part of buying and selling
                profit+=currentmax-currentmin       #calculate the currentprofit and add to the total profit
                currentmax=prices[i]                #reset currentmax to current value
                currentmin=prices[i]                #reset currentmin to current value
            
        profit+=currentmax-currentmin               #add the last part of profit to total profit
                
        return profit
        
        
            
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #Say you have an array for which the ith element is the price of a given stock on day i.
        #Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times). 
        #However, you may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
