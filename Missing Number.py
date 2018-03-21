class Solution(object):
    # bit manipulation solution , XOR
    def missingNumber(self, nums):
        length = len(nums)
        for i,n in enumerate(nums):
            length ^= i^n
        
        return length
        
    
    # sum solution
    # def missingNumber(self, nums):
    #     length = len(nums)
    #     return (length*(length+1))/2 - sum(nums)
    
    
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
# Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

