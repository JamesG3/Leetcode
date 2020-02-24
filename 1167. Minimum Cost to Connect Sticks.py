import heapq

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res = 0
        
        if len(sticks) < 2:
            return 0
        
        while len(sticks) > 1:
            mini1 = heapq.heappop(sticks)
            mini2 = heapq.heappop(sticks)
            res += mini1 + mini2
            heapq.heappush(sticks, mini1 + mini2)
        
        return res
            
'''
You have some sticks with positive integer lengths.
You can connect any two sticks of lengths X and Y into one stick by paying a cost of X + Y.  You perform this action until there is one stick remaining.
Return the minimum cost of connecting all the given sticks into one stick in this way.

Solution: Heap
Time: O(nlogn)
'''
