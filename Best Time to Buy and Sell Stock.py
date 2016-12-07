class Solution(object):
    def maxProfit(self, prices):
        if len(prices)==0:
            return 0
        currentmax=prices[-1]
        currentprofit=0
        maxprofit=0
        
        for i in range(len(prices)-1, -1, -1):          #from latest price to eariler price
            if prices[i]>currentmax:
                currentmax=prices[i]
            if prices[i]<currentmax:
                currentprofit=currentmax-prices[i]      #calculate the current profit
                maxprofit=max(maxprofit, currentprofit) #update the maxprofit with the larger one
                
        return maxprofit
            
        """
        :type prices: List[int]
        :rtype: int
        """
        
        #Say you have an array for which the ith element is the price of a given stock on day i.
        #If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.
        #Example: Input: [7, 1, 5, 3, 6, 4], Output: 5
        #max:6-1=5
