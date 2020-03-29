import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.hp = []
        heapq.heapify(self.hp)
        for n in nums:
            self.heap(n)
        
    def heap(self, n):
        heapq.heappush(self.hp, n)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp)
        
    def add(self, val: int) -> int:
        self.heap(val)
        res = heapq.heappop(self.hp)
        heapq.heappush(self.hp, res)
        return res
    
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

'''
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Your KthLargest class will have a constructor which accepts an integer k and an integer array nums, which contains initial elements from the stream. For each call to the method KthLargest.add, return the element representing the kth largest element in the stream.

Solution: Heap, Priority queue, maintain a size K min heap, the top of heap is the answer
Time: O(logk)
Space: O(k)
'''
