class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        self.D = D
        self.weights = weights
        
        small, large = max(weights), sum(weights)
        while small <= large:
            mid = (small + large) // 2
            if self.if_works(mid):
                large = mid - 1
            else:
                small = mid + 1
        
        # smaller will be the larger one after this while loop 
        return small
        
        
        
    def if_works(self, weight):
        day_counter = 1
        cur_load = 0
        
        for w in self.weights:
            # early termination
            if day_counter > self.D:
                return False
            
            cur_load += w
            if cur_load > weight:
                day_counter += 1
                cur_load = w
        
        if day_counter > self.D:
            return False
        else:
            return True
'''
A conveyor belt has packages that must be shipped from one port to another within D days.
The i-th package on the conveyor belt has a weight of weights[i].  Each day, we load the ship with packages on the conveyor belt (in the order given by weights). We may not load more weight than the maximum weight capacity of the ship.
Return the least weight capacity of the ship that will result in all the packages on the conveyor belt being shipped within D days.

Solution: Binary Search, check if there is a weight in range[small, large] works
Time: O(n * log(n))
Space: O(1)
'''        
