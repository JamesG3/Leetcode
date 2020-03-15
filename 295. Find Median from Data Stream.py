import heapq
class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_heap = []
        self.max_heap = []
        heapq.heapify(self.max_heap)
        heapq.heapify(self.min_heap)

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == 0 and len(self.min_heap) == 0:
            heapq.heappush(self.min_heap, num)
            return
        
        if len(self.max_heap) == 0 or len(self.min_heap) == 0:
            if len(self.max_heap) == 0:
                v = heapq.heappop(self.min_heap)
            elif len(self.min_heap) == 0:
                v = - heapq.heappop(self.max_heap)
            v, num = sorted([v, num])
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, -v)
            return
        
        else:
            min_top, max_top = heapq.heappop(self.min_heap), - heapq.heappop(self.max_heap)
            v1, v2, v3 = sorted([min_top, max_top, num])
            
            if len(self.min_heap) > len(self.max_heap):
                heapq.heappush(self.max_heap, - v1)
                heapq.heappush(self.max_heap, - v2)
                heapq.heappush(self.min_heap, v3)
                
            elif len(self.min_heap) < len(self.max_heap):
                heapq.heappush(self.max_heap, - v1)
                heapq.heappush(self.min_heap, v2)
                heapq.heappush(self.min_heap, v3)
                
            else:
                heapq.heappush(self.max_heap, - v1)
                heapq.heappush(self.min_heap, v2)
                heapq.heappush(self.min_heap, v3)
                
            return
                

    def findMedian(self) -> float:
        
        if len(self.min_heap) == len(self.max_heap):
            v1, v2 = heapq.heappop(self.min_heap), - heapq.heappop(self.max_heap)
            heapq.heappush(self.min_heap, v1)
            heapq.heappush(self.max_heap, - v2)
            return (v1 + v2) / 2
        
        elif len(self.min_heap) > len(self.max_heap):
            v = heapq.heappop(self.min_heap)
            heapq.heappush(self.min_heap, v)
            return v
        else:
            v = - heapq.heappop(self.max_heap)
            heapq.heappush(self.max_heap, - v)
            return v
            
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



'''
Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value. So the median is the mean of the two middle value.

Solution: Two heaps, min_heap and max_heap to keep the median(s) in the top of heaps
Time: O(h) findMedian, O(h) addNum
Space: O(n)
'''
