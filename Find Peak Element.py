class Solution(object):
    # binary search solution, O(lgn), O(1)
    def findPeakElement(self, nums):
        l, r = 0, len(nums)-1
        
        while l<r:
            m = (l+r) / 2
            if nums[m] < nums[m+1]:
                l = m+1
            else:
                r = m
        return l
        
        
        
        """
        :type nums: List[int]
        :rtype: int
        """
        # find the peak element and return it's index, in O(logn)
