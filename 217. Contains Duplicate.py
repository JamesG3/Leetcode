class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        Solution: Hash Set
        Time: O(n)
        Space: O(n)
        """
        return len(nums) != len(set(nums))
    
# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
