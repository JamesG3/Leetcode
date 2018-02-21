class Solution(object):
    def minCostClimbingStairs(self, cost):
        length = len(cost)
        if length == 0:
            return 0
        
        dp = cost[:2]                       # minimum cost sum to reach the current location
        for i in xrange(2, length):         # always choose the path with lower cost
            dp.append(min(dp[-1] + cost[i], dp[-2] + cost[i]))
            
        return min(dp[-2:])        
            
        
        """
        :type cost: List[int]
        :rtype: int
        """
        
        
        #On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
        # Once you pay the cost, you can either climb one or two steps. 
        # You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.
