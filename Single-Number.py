class Solution(object):
    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums)
        
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #Given an array of integers, every element appears twice except for one. Find that single one.
        
