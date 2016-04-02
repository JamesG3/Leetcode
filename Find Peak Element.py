class Solution(object):
    def findPeakElement(self, nums):
        return nums.index(max(nums))
        """
        :type nums: List[int]
        :rtype: int
        """
        #Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.
