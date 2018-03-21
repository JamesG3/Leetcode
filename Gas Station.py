class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        length = len(gas)
        res = 0
        total = 0
        diff = 0
        
        for i in xrange(length):
            diff += gas[i] - cost[i]
            total += gas[i] - cost[i]
            
            if diff < 0:                # if diff smaller than 0, then start from next station
                diff = 0
                res = i+1
            
        if total < 0:
            return -1
        return res
                
            
        
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        
        # There are N gas stations along a circular route, where the amount of gas at station i is gas[i].
        # You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.
        # Return the starting gas station's index if you can travel around the circuit once, otherwise return -1.

