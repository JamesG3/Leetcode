class Solution(object):
    def singleNumber(self, nums):
        return (sum(set(nums))*3 - sum(nums)) / 2     #useful prerequisite: every element appears three times except for one
        
        
        """
        :type nums: List[int]
        :rtype: int
        
        Given an array of integers, every element appears three times except for one. Find that single one.
        """
        
