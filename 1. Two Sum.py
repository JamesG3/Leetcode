class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i_dict = {}
        for i, n in enumerate(nums):
            if (target-n) in i_dict:
                return [i, i_dict[target-n]]
            else:
                i_dict[n] = i
'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Solution: Hashtable
Time, Space: O(n)
'''
