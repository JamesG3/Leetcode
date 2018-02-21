class Solution(object):
    def minCost(self, costs):
        length = len(costs)
        if length == 0:
            return 0
        
        dp = [costs[0]]
        
        for j in xrange(1, length):
            tmp = []
            
            for i in xrange(3):
                if i == 0:
                    tmp.append(min(dp[-1][1] + costs[j][0], dp[-1][2] + costs[j][0]))
                elif i == 1:
                    tmp.append(min(dp[-1][0] + costs[j][1], dp[-1][2] + costs[j][1]))
                elif i == 2:
                    tmp.append(min(dp[-1][0] + costs[j][2], dp[-1][1] + costs[j][2]))
            dp.append(tmp)
            
        
        return min(dp[-1])
        
        
        
        """
        :type costs: List[List[int]]
        :rtype: int
        """
