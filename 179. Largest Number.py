class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        Solution: Using cmp lambda as the self-defined comparsion method, sort by the value of string
        Time: O(logn)
        Space: O(n)
        """
        nums = [str(n) for n in nums]
        return ''.join(sorted(nums, cmp = lambda x, y: 1 if x+y < y+x else -1)).lstrip('0') or '0'
        
        
# Given a list of non negative integers, arrange them such that they form the largest number.
# For example, given [3, 30, 34, 5, 9], the largest formed number is 9534330.
