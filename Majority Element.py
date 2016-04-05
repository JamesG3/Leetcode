class Solution(object):
    def majorityElement(self, nums):
        return sorted(nums)[len(nums)/2]
        """
        :type nums: List[int]
        :rtype: int
        """
#Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
