class Solution(object):
    def findKthLargest(self, nums, k):          #one line solution
        return sorted(nums)[-k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        
        
       # heap solution, slower
    def findKthLargest(self, nums, k):
        length = len(nums)
        if not length or k > length:
            return -1
        
        heap = []
        for n in nums:
            heappush(heap, -n)
            
        for i in xrange(k-1):
            heappop(heap)
            
        return -heappop(heap)
        # Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element. 
