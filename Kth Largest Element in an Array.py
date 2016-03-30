class Solution(object):
    def findKthLargest(self, nums, k):          #one line solution
        return sorted(nums)[-k]
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element. 
