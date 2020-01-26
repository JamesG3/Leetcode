class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = prev_max = prev_min = nums[0]
        for n in nums[1:]:
            # catch the negativae value with the largest abs value
            cur_min = min(n, n*prev_max, n*prev_min)
            cur_max = max(n, n*prev_max, n*prev_min)
            res = max(res, cur_max)
            
            prev_max = cur_max
            prev_min = cur_min
            
        return res
        
'''
Given an integer array nums, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Solution: Greedy, capture the max and min value in every step
Time: O(n)
Space: O(1)
'''
